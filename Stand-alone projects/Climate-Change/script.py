# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:26:04 2020

@author: wyckliffe
"""


# import modules 
import matplotlib.pyplot as plt 
import numpy as np 
from sklearn.linear_model import LinearRegression 
import seaborn as sns 


class Climate(): 
    
    def __init__(self, yearsBase, meanBase, years , mean): 
        
        self.yearsBase = yearsBase
        self.meanBase = meanBase
        self.years = years
        self.mean = mean 
        
    def scatterPlot(self): 
        
        plt.scatter(self.yearsBase, self.meanBase)
        plt.title('scatter plot of mean temp difference vs year')
        plt.xlabel('years', fontsize=12)
        plt.ylabel('mean temp difference', fontsize=12)
        plt.show()
        
       
    def f(self, x): 
        
        # Create a linear regression from the data points
        m,b = np.polyfit(self.yearsBase, self.meanBase, 1)
        return m*x + b
        
    def numpyLinearRegression(self): 
        m,b = np.polyfit(self.yearsBase, self.meanBase, 1)
        
        plt.scatter(self.yearsBase, self.meanBase)
        plt.plot(self.yearsBase, self.f(self.yearsBase))
        plt.title('scatter plot of mean temp difference vs year')
        plt.xlabel('years', fontsize=12)
        plt.ylabel('mean temp difference', fontsize=12)
        plt.show()

        # Prints text to the screen showing the computed values of m and b
        print(' y = {0} * x + {1}'.format(m, b))
        plt.show()
        
    def sklearnLinerRegression(self): 
        
        # Pick the Linear Regression model and instantiate it
        model = LinearRegression(fit_intercept=True)

        # Fit/build the model
        model.fit(self.yearsBase[:, np.newaxis], self.meanBase)
        mean_predicted = model.predict(self.yearsBase[:, np.newaxis])

        # Generate a plot like the one in the previous exercise
        plt.scatter(self.yearsBase, self.meanBase)
        plt.plot(self.yearsBase, mean_predicted)
        plt.title('scatter plot of mean temp difference vs year')
        plt.xlabel('years', fontsize=12)
        plt.ylabel('mean temp difference', fontsize=12)
        plt.show()

        print(' y = {0} * x + {1}'.format(model.coef_[0], model.intercept_))
        
    def tempDifference(self): 
        
        plt.scatter(self.years, self.mean)
        plt.title('scatter plot of mean temp difference vs year')
        plt.xlabel('years', fontsize=12)
        plt.ylabel('mean temp difference', fontsize=12)
        sns.regplot(self.yearsBase, self.meanBase)
        plt.show()
        
        
# import data 
yearsBase, meanBase = np.loadtxt('5-year-mean-1951-1980.csv', delimiter=',', usecols=(0, 1), unpack=True)
years, mean = np.loadtxt('5-year-mean-1882-2014.csv', delimiter=',', usecols=(0, 1), unpack=True)

# initialize the class 
climate = Climate(yearsBase, meanBase, years, mean)