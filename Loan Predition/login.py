import pandas as pd
import pickle
def validate_login(username, password):
    df = pd.read_csv('login.csv')
    user = df[(df['username'] == username) & (df['password'] == password)]
    return not user.empty