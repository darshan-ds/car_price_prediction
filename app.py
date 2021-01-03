from flask import Flask, render_template, request
import jsonify
import requests
import pickle
import numpy as np
import sklearn
from sklearn.preprocessing import StandardScaler
app = Flask(__name__)
model = pickle.load(open('random_forest_regression_model.pkl', 'rb'))
@app.route('/',methods=['GET'])
def Home():
    return render_template('index.html')


standard_to = StandardScaler()
@app.route("/predict", methods=['POST'])
def predict():
    if request.method == 'POST':
        Year = int(request.form['Year'])
        Year=2020-Year
        
        Kms_Driven=int(request.form['Kms_Driven'])
        
        Owner = request.form['Owner']
        td = 0
        s = 0
        t = 0
        fth = 0
        if Owner == 'fst':
            pass
        elif Owner == 'td':
            td=1
        elif Owner == 's':
            s=1
        elif Owner == 't':
            t=1
        else:
            fth=1
        
        
        Fuel_Type_Petrol=request.form['Fuel_Type_Petrol']
        fuel_Petrol = 0
        fuel_Diesel = 0
        fuel_LPG = 0
        fuel_Electric = 0
        if Fuel_Type_Petrol == 'Petrol':
            fuel_Petrol=1
        elif Fuel_Type_Petrol == 'Diesel':
            fuel_Diesel=1
        elif Fuel_Type_Petrol  == 'LPG':
            fuel_LPG=1
        elif Fuel_Type_Petrol == 'Eletric':
            fuel_Electric=1
        else:
            pass
        
        
        ind = 0
        tdeal = 0
        Seller_Type_Individual=request.form['Seller_Type_Individual']
        if(Seller_Type_Individual=='Ind'):
            ind = 1
        elif Seller_Type_Individual=='tdeal':
            tdeal = 1
        else:
            pass
            
        Transmission_Manual=request.form['Transmission_Manual']
        if(Transmission_Manual=='Manual'):
            Transmission_Manual=1
        else:
            Transmission_Manual=0
          
            
        prediction = model.predict([[Kms_Driven,Year,fuel_Diesel,fuel_Electric,fuel_LPG,fuel_Petrol,ind,tdeal,Transmission_Manual,fth ,s ,td , t]])  
            
        output=round(prediction[0],2)
        if output<0:
            return render_template('index.html',prediction_texts="Sorry you cannot sell this car")
        else:
            return render_template('index.html',prediction_text="You Can Sell The Car at {}".format(output))
    else:
        return render_template('index.html')

if __name__=="__main__":
    app.run(debug=True)

