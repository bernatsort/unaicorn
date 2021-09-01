#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
# Split the data into our train and test or train and validation data sets. 
# we use sklearn (library) and access to model_selection (the module) 
# to get the function train_test_split 
from sklearn.model_selection import train_test_split
# pickle is really useful for saving our model (all the parameters that are being saved).
import pickle
from sklearn.ensemble import RandomForestClassifier
# from sklearn.metrics import accuracy_score 


# Load the .csv
df = pd.read_csv('C:/Users/Bernat/Desktop/Bernat/7. Full stack web development and AI with Python (Django)/Data Science/titanic/train.csv')

# The name is very long, so we can use the title: 
# So that might be a helpful indicator to whether someone survived or not with: Mr. and Mrs., Miss or other ones like that. 
def get_title(name):
    if '.' in name:
        return name.split(',')[1].split('.')[0].strip()
    else:
        return 'Unknown'

# There are a lot of titles. We should condense or reduce it.
def shorter_titles(x):
    title = x["Title"]
    # We can group those into Officer
    if title in ['Capt', 'Col', 'Major']:
        return 'Officer'
    # There are some for royalty: 
    elif title in ['Jonkheer', 'Don', 'the Countess', 'Dona', 'Lady', 'Sir']:
        return 'Royalty'
    elif title == 'Mme':
        return 'Mrs'
    elif title in ['Mlle', 'Ms']:
        return 'Miss'
    else: 
        return title
    
    
    
# we're going to be taking the actual titles from the names, 
# so we're going to be creating a new column and that will contain the only the titles from the names
df['Title'] = df['Name'].map(lambda x: get_title(x))
# apply: apply this function to all of the values in this column 
# axis=1 --> go down the column, not go along a row. 
df['Title'] = df.apply(shorter_titles, axis=1)
# getting the IDs
# ids = df['PassengerId']


# In this column, fill any of the NA or not applicable values, 
# and I just want to fill those with the median.
# inplace=True --> make that change happen.
df['Age'].fillna(df['Age'].median(), inplace=True)
df['Fare'].fillna(df['Fare'].median(), inplace=True)
df['Embarked'].fillna("S", inplace=True)
# For 'Cabin', 'Ticket', 'Name'  I'm just going to be dropping it simply because 
# there were so many NA values, it is not very usefull, and we already have the title, respectively. 
df.drop("Cabin", axis=1, inplace=True)
df.drop("Ticket", axis=1, inplace=True)
df.drop("Name", axis=1, inplace=True)
# We have to change our categorical values into numeric values 
# because with our machine learning model, everything has to be a number.
df.Sex.replace(('male','female'), (0,1), inplace = True)
df.Embarked.replace(('S','C','Q'), (0,1,2), inplace = True)
df.Title.replace(('Mr','Miss','Mrs','Master','Dr','Rev','Officer','Royalty'), (0,1,2,3,4,5,6,7), inplace = True)



# Split the data frame into X and Y
# Y: dependent variable
y = df['Survived']
# X: independent variable
# df.drop: I take all the data frame except the columns I've dropped. 
# axis = 1: I want to drop the whole column, not the row.
X = df.drop(['Survived', 'PassengerId'], axis=1)
# First of all, we're creating variables.
    # (write them in this order)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1)
# Store the model (randomforest)
randomforest = RandomForestClassifier()
# .fit(): I have my model. It doesn't have any parameters. It hasn't ever seen any data.
#         Now I want you to train it. It's going to be essentially training.
randomforest.fit(X_train, y_train)
# I want make predictions, and see if my y validation is accurate or not.
y_pred = randomforest.predict(X_test)

# Calculating the accuracy: taking an accuracy score.
# Putting in the y predictions, comparing them to the actual ground truth, 
# which is what we have in the data (y_test). 
# acc_randomforest = round(accuracy_score(y_pred, y_test)*100, 2)
# Print out the accuracy 
# print("Accuracy: {}".format(acc_randomforest))


# Save the model (randomforest)
# Write files: open('name_of_model.sav', 'wb') where 'wb' --> write binary
filename = 'training_model.sav'
pickle.dump(randomforest, open(filename, 'wb'))

