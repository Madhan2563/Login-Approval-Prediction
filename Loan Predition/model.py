import numpy as np
import pandas as pd
import pickle 
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
df=pd.read_csv('data.csv')
df['loan_status']=df['loan_status'].map({
    ' Approved':1,
    ' Rejected':0})
x=df[['no_of_dependents','income_annum','loan_amount','loan_term','cibil_score','residential_assets_value','commercial_assets_value','luxury_assets_value','bank_asset_value']]
y=df['loan_status']
model=DecisionTreeClassifier(
    criterion='entropy',
    max_depth=5,
    random_state=42
)
model.fit(x,y)
pickle.dump(model,open('model.pkl','wb'))
print('Model trained and saved successfully.')
print('Model Accuracy:',accuracy_score(y,model.predict(x))*100)