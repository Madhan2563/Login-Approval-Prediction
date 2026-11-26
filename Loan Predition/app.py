import os
import pickle
from flask import Flask, redirect,render_template,request
import numpy as np
from login import validate_login
import pandas as pd
global loan_id
global user_id
app=Flask(__name__)
model=pickle.load(open('model.pkl','rb'))
@app.route("/")
def home():
        return render_template("login.html")
@app.route("/logout")
def logout():
    return redirect("/")
@app.route("/login",methods=['GET','POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    valid=validate_login(username, password)
    if  valid:
           return redirect("/home")
    else:
        return render_template("login.html",error="Invalid username or password. Please try again.")
@app.route("/regi",methods=['GET','POST'])
def regi():
    email = request.form.get('email')
    username = request.form.get('username')
    password = request.form.get('password')
    emp_status = request.form.get('emp_status')
    df=pd.read_csv('login.csv')
    user_id=df['user_id'].max()+1
    loan_id=df['loan_id'].max()+1
    with open('login.csv', 'a') as f:
        f.write(f"{user_id},{username},{password},{email},{emp_status},{loan_id}\n")
    return redirect("/")
@app.route("/home")
def home_page():
    return render_template("home.html")     
@app.route("/register")
def register():
    return render_template("register.html")
@app.route("/index")
def predictor_page():
    return render_template("predictor.html")
@app.route("/predictor",methods=['GET','POST'])
def predictor():
    df=pd.read_csv('login.csv')
    loan_id= df['loan_id'].max()
    input=[int(x) for x in request.form.values()]
    final=np.array(input)
    prediction=model.predict(final.reshape(1,-1))
    output=prediction[0]
    if(output==1):
        loan_status="Approved"
    else:   
        loan_status="Rejected"
    with open('user_data.csv', 'a') as f:
        f.write(f"{loan_id},{input[0]},{input[1]},{input[2]},{input[3]},{input[4]},{input[5]},{input[6]},{input[7]},{input[8]},{loan_status}\n")
    return render_template("result.html", loan_status=loan_status)
@app.route("/about")
def about():
    return render_template("about.html")

if __name__=="__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
