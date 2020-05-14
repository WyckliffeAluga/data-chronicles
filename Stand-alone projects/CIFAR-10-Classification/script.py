# -*- coding: utf-8 -*-
"""
Created on Sat May  9 20:38:30 2020

@author: wyckl
"""

# import libraries 
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import seaborn as sns
from keras.datasets import cifar10
import random

class CNN(): 
    
    def __init__(self): 
        
        (self.x_train, self.y_train), (self.x_test, self.y_test) = cifar10.load_data()
        assert(self.x_train.shape[0] == self.y_train.shape[0]), "X training data is not equal to y_training data"
        
    
    def visualize(self): 
        

        fig, ax = plt.subplots(5, 5, figsize=(25,25))
        fig.tight_layout() 
        ax = ax.ravel()
        
        for i in range(25): 
            random_idx = random.randint(0, len(self.x_train) - 1)
            ax[i].imshow(self.x_train[random_idx])
            ax[i].set_title((self.label(self.y_train[random_idx][0])))
            ax[i].axis("Off")
        
    def label(self, class_no): 
        
        switcher = {
                    0:"Airplane", 
                    1:"Car", 
                    2:"Bird", 
                    3:"Cat", 
                    4:"Deer", 
                    5:"Dog", 
                    6:"Frog", 
                    7:"Horse", 
                    8:"Ship", 
                    9:"Truck"
                    }
        return switcher.get(class_no, "Invalid class")
    
    def imgPrep(self, img): 
        img = img.astype("float32")
        
        

c = CNN()