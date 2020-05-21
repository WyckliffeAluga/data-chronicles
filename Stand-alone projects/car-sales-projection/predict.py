# -*- coding: utf-8 -*-
"""
Created on Sat May  9 19:52:11 2020

@author: wyckliffe
"""
from sklearn.preprocessing import  MinMaxScaler
from keras.models import load_model
import numpy as np 


def predict(Gender, Age, Salary, Debt, Net): 
    
    if Gender == "M" or Gender == "m" : 
        Gender = 1 
    else: 
        Gender = 0 
    
    
    inputs = np.asarray([Gender, Age, Salary, Debt, Net]).reshape(-1,1)
    
    scaler = MinMaxScaler()
    inputs = scaler.fit_transform(inputs)
    inputs = inputs.T
    
    model = load_model("model.h5")
 
    predictions = model.predict(inputs)
    
    prediction =  scaler.inverse_transform(predictions)
    
    amount = prediction[0][0]
    
    return '${:,.2f}'.format(amount)
    
   