# -*- coding: utf-8 -*-
"""
Created on Sat May  9 18:29:38 2020

@author: wyckliffe
"""

# import modules 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import  MinMaxScaler
from sklearn.model_selection import train_test_split
import tensorflow.keras
import tensorflow as tf
from keras.models import  Sequential, load_model
from keras.layers import  Dense



class ANN(): 
    
    def __init__(self): 
        
        self.data = self.get_data() 
        
        self.clean_data = self.clean()
        
        self.X , self.y = self.split()
        
        self.X_scaled, self.y_scaled = self.scale()     
        
        self.x_train , self.x_test, self.y_train, self.y_test = train_test_split(self.X_scaled, 
                                                             self.y_scaled, 
                                                             test_size=0.15, 
                                                             random_state=123)
        
        # self.model()
        
    def get_data(self):
        
        df = pd.read_csv("Car_Purchasing_Data.csv", encoding="ISO-8859-1")
        
        return df
    
    def visualize(self): 
        
        sns.pairplot(self.data)
    
    def clean(self): 
        
        return self.data.drop(['Customer Name', 
                                          'Customer e-mail',
                                          "Country"], axis=1)
    def split(self): 
        X = self.clean_data.drop(['Car Purchase Amount'], axis=1)
        y = self.data['Car Purchase Amount']
        
        return X, y 
    
    def scale(self): 
        scaler = MinMaxScaler()
        
        return scaler.fit_transform(self.X) , scaler.fit_transform(self.y.values.reshape(-1,1))
    
    def model(self): 
        

        model = Sequential() 
        model.add(Dense(40, input_dim = 5, activation='relu'))
        model.add(Dense(40, activation='relu'))
        model.add(Dense(1, activation='linear'))
                
        model.compile(optimizer = 'adam', loss='mse' )
        model.fit(self.x_train, self.y_train , 
                  epochs=100, batch_size=25, verbose=1, shuffle=1, 
                  validation_split=0.2)
        
        model.save("model.h5")
        print('Model Saved!')
        
        
    def progress(self): 
        hist = load_model("model.h5")
        
        plt.plot(hist.history['loss'])
        plt.plot(hist.history['val_loss'])
        plt.legend(['loss', 'validation loss'])
        plt.xlabel("Epochs")
        plt.show()
        
    def evaluate(self): 
        
        model = load_model("model.h5")
        score = model.evaluate(self.x_test, self.y_test , verbose=1)
        
        return score
        
        
a = ANN()
