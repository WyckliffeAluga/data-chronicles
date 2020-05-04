# -*- coding: utf-8 -*-
"""
Created on Mon May  4 15:49:18 2020

@author: wyckliffe
"""


from keras.datasets import imdb as imdb
from keras.preprocessing import sequence
from keras.models import Sequential
from keras.layers import Dense
from keras.layers.embeddings import Embedding
from keras.layers import Flatten

import seaborn as sns
import matplotlib.pyplot as plt

import string 
import numpy as np 



class Sentiment(): 
    
    def __init__(self, x_train, y_train, x_test, y_test ):
        
      super(Sentiment, self).__init__()
      self.x_train = x_train 
      self.x_test  = x_test 
      self.y_train = y_train 
      self.y_test  = y_test
    
    def wordMapper(self): 
        
        """
        Mapping words to integers 
        """
        
        word_dict = imdb.get_word_index()
        word_dict = { key : (value + 3) for key, value in word_dict.items()}
        word_dict['']  = 0  # Padding
        word_dict['>'] = 1 # Start
        word_dict['?'] = 2 # Unknown word
        reverse_word_dict = {value : key for key, value in word_dict.items()}
        
        print(" ".join(reverse_word_dict[id] for id in self.x_train[0]))
        
    def nn(self):
        
        # clean data
        max_review_length = 500
        x_train = sequence.pad_sequences(self.x_train, maxlen=max_review_length)
        x_test = sequence.pad_sequences(self.x_test, maxlen=max_review_length)
        
        # build the model 
        embedding_vector_length = 32
        
        model = Sequential()
        model.add(Embedding(top_words, embedding_vector_length, input_length=max_review_length))
        model.add(Flatten())
        model.add(Dense(16, activation='relu'))
        model.add(Dense(16, activation='relu'))
        model.add(Dense(1, activation='sigmoid'))
        model.compile(loss='binary_crossentropy',optimizer='adam', metrics=['accuracy'])
        
        return model
        
    def hist(self):
        
        return self.nn.fit(x_train, y_train, validation_data=(x_test, y_test), epochs=5, batch_size=128)


        
# prep dataset 
top_words = 10000

(x_train, y_train), (x_test, y_test) = imdb.load_data(num_words=top_words)

# initialize sentiment class 

sentiment = Sentiment(x_train, y_train, x_test, y_test)

model = sentiment.nn()

class training(): 
    
    def __init__(self, model):
        
        self.model = model 
        
    def trainingPlot(self):
        
        acc = self.model.history['accuracy']
        val = self.model.history['val_accuracy']
        epochs = range(1, len(acc) + 1)
        
        plt.plot(epochs, acc, '-', label='Training accuracy')
        plt.plot(epochs, val, ':', label='Validation accuracy')
        plt.title('Training and Validation Accuracy')
        plt.xlabel('Epoch')
        plt.ylabel('Accuracy')
        plt.legend(loc='upper left')
        plt.plot()
        

class Analyze(): 
    
    def __init__(self, model): 
        
        self.model = model 
        
    def textAnalyzer(self , text): 
        
        # Prepare the input by removing punctuation characters, converting
        # characters to lower case, and removing words containing numbers
        
        word_dict = imdb.get_word_index()
        max_review_length = 500
        
        translator = str.maketrans('', '', string.punctuation)
        text = text.translate(translator)
        text = text.lower().split(' ')
        text = [word for word in text if word.isalpha()]
    
        # Generate an input tensor
        input = [1]
        for word in text:
            if word in word_dict and word_dict[word] < top_words:
                input.append(word_dict[word])
            else:
                input.append(2)
        padded_input = sequence.pad_sequences([input], maxlen=max_review_length)
    
        # Invoke the model and return the result
        result = self.model.predict(np.array([padded_input][0]))[0][0]
        return result
    
# initialize analyze
an = Analyze(model)


        
        
