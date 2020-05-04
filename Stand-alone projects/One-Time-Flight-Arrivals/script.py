import pandas as pd
import  math
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import roc_auc_score , confusion_matrix ,  precision_score , recall_score , roc_curve
import matplotlib.pyplot as plt 
import numpy as np

df = pd.read_csv("flightdata.csv")

# clean the data
df = df.drop("Unnamed: 25" , axis=1)
df = df[["MONTH", "DAY_OF_MONTH", "DAY_OF_WEEK", "ORIGIN", "DEST", "CRS_DEP_TIME", "ARR_DEL15"]] # the important features
df = df.fillna({"ARR_DEL15" : 1})

# bin the departure time
for index , row in df.iterrows():
    df.loc[index, "CRS_DEP_TIME"] = math.floor(row["CRS_DEP_TIME"] / 100 )

# deal with the categorical datasets
df = pd.get_dummies(df, columns=["ORIGIN", "DEST"])

# prepare the data for modelling
train_x, test_x, train_y, test_y = train_test_split(df.drop("ARR_DEL15" , axis=1), df["ARR_DEL15"] , test_size=0.2, random_state=42)

# model

rf = RandomForestClassifier(random_state=13)
rf.fit(train_x, train_y)

class Flight():
    """docstring for ."""

    def __init__(self, model, x_test, y_test, x_train , y_train):
        super(Flight, self).__init__()
        self.model = model
        self.x_test = x_test
        self.y_test = y_test 
        self.x_train= x_train
        self.y_train= y_train
        
    def predicted(self): 
        
        return self.model.predict(self.x_test)
    
    def score(self): 
        
        return self.model.score(self.x_test, self.y_test)
    
    
    def roc(self): 
        probabilities = self.model.predict_proba(self.x_test)
        return roc_auc_score(self.y_test, probabilities[:,1])
    
    def matrix(self): 
        
        return confusion_matrix(self.y_test ,self.predicted())
    
    def precision(self): 
        
        train_predictions = self.model.predict(self.x_train)
        return precision_score(self.y_train , train_predictions )
    
    def recall(self): 
        
        train_predictions = self.model.predict(self.x_train)
        return recall_score(self.y_train , train_predictions)
    
    def curve(self): 
    
        probabilities = self.model.predict_proba(self.x_test)
        fpr, tpr, _ = roc_curve(self.y_test, probabilities[:,1])
        plt.plot(fpr, tpr)
        plt.plot([0, 1], [0, 1], color='grey', lw=1, linestyle='--')
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.show()
        

flight = Flight(rf, test_x, test_y , train_x , train_y) 

def predict_delay(departure_date_time, origin, destination): 
    
    from datetime import datetime 
    
    try: 
        departure_date_time_parsed = datetime.strptime(departure_date_time, '%d/%m/%Y %H:%M:%S' )
    except ValueError as e: 
        return "Error parsing date/time - ".format(e)
    
    month  = departure_date_time_parsed.month 
    day    = departure_date_time_parsed.day 
    day_of_week = departure_date_time_parsed.isoweekday()
    hour = departure_date_time_parsed.hour 
    
    origin = origin.upper()
    destination = destination.upper() 
    
    input = [{'MONTH': month,
              'DAY': day,
              'DAY_OF_WEEK': day_of_week,
              'CRS_DEP_TIME': hour,
              'ORIGIN_ATL': 1 if origin == 'ATL' else 0,
              'ORIGIN_DTW': 1 if origin == 'DTW' else 0,
              'ORIGIN_JFK': 1 if origin == 'JFK' else 0,
              'ORIGIN_MSP': 1 if origin == 'MSP' else 0,
              'ORIGIN_SEA': 1 if origin == 'SEA' else 0,
              'DEST_ATL': 1 if destination == 'ATL' else 0,
              'DEST_DTW': 1 if destination == 'DTW' else 0,
              'DEST_JFK': 1 if destination == 'JFK' else 0,
              'DEST_MSP': 1 if destination == 'MSP' else 0,
              'DEST_SEA': 1 if destination == 'SEA' else 0 }]
    
    return rf.predict_proba(pd.DataFrame(input))[0][0]

# sample trying

labels = ('Oct 1', 'Oct 2', 'Oct 3', 'Oct 4', 'Oct 5', 'Oct 6', 'Oct 7')
values = (predict_delay('1/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('2/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('3/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('4/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('5/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('6/10/2018 21:45:00', 'JFK', 'ATL'),
          predict_delay('7/10/2018 21:45:00', 'JFK', 'ATL'))

alabels = np.arange(len(labels))

plt.bar(alabels, values, align='center', alpha=0.5)
plt.xticks(alabels, labels)
plt.ylabel('Probability of On-Time Arrival')
plt.ylim((0.0, 1.0))
