import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn import metrics
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.linear_model import LogisticRegression
from imblearn.over_sampling import RandomOverSampler

import warnings
warnings.filterwarnings('ignore')

#imaport data
df = pd.read_csv('ML learn/austin_weather.csv')
#print("First 5 rows ",df.head())
#print("Data shape is ",df.shape)
#print("Info on the data ", df.info())
#print(df.describe())
#print(df.describe().T)
#print(df.isnull().sum())
#print(df.columns)

for col in df.columns:
# Checking if the column contains
# any null values
    if df[col].isnull().sum() > 0:
        val = df[col].mean()
        df[col] = df[col].fillna(val)
          
	
print(df.isnull().sum().sum())
data_rainfall = df.copy()
#print(df["Events"])

for item in range(0,len(df["Events"])):
    if "Rain" in df["Events"].iloc[item]:
        df["Events"].iloc[item] = 1
    else:
        df["Events"].iloc[item] = 0

print(df["Events"].iloc[0])

print("Data tyoe is ",type(df["Events"].iloc[0]))
print(df)

# Number of dry days
count = 0
for item in range(0,len(df["Events"])):
    if df["Events"].iloc[item] == 1:
        count = count+1
    else:
       count= count
   
weather_type = ["Wet days total is " +str(count),"Dry days total is " +str(len(df["Events"])-count)]
data = [ count,(len(df["Events"]))-count]
title_main = "Weather in Austin Texas between " +str(df["Date"].loc[0]) +" and " +str(df["Date"].iloc[-1])
# Creating plot

fig = plt.figure(figsize=(10, 7))
plt.pie(data, labels=weather_type)
plt.title(title_main)
# show plot
plt.show()