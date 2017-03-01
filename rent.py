
# coding: utf-8

# In[54]:

import urllib
import csv
import io
import pandas as pd
import numpy as np

from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Ridge, RidgeCV
from sklearn.model_selection import train_test_split, cross_val_score, KFold, GridSearchCV
from sklearn.pipeline import Pipeline


def score_rent():
    """"""
    """"""
    
    
#Download the csv file and store it as a pandas dataframe


    data = urllib.request.urlopen('https://ndownloader.figshare.com/files/7586326')
    f = csv.reader(io.TextIOWrapper(data))
    dataset = list(f)
    df = pd.DataFrame(dataset)
    
    
#Assign row 0 to the be the column names
#Drop the feature columns that are related to occupants and not apartments
#Drop the feature columns that are related to owner occupied properties
#Drop rows for which the "Monthly Contract Rent" column (the response variable) has a missing value
#Drop rows with missing values


    df.columns = df.iloc[0]
    dropped = [0] + list(range(30,44)) + list(range(45,65)) + [89,90,93,94,95,96,97,98,113,114,115,116] + list(
    range(119,124)) + list(range(130,136)) + list(range(140,162)) + list(range(163,197)) + list(range(80,89))

    df = df.drop(df[df.uf17 == '99999'].index)
    df = df.drop(df.columns[[dropped]], axis = 1)
    df = df.drop(df[df.uf1_1 == '8'].index)
    df = df.drop(df[df.uf1_7 == '8'].index)
    df = df.drop(df[df.uf1_12 == '8'].index)
    df = df.drop(df[df.uf1_17 == '8'].index)
    df = df.drop(df[df.sc23 == '8'].index)
    df = df.drop(df[df.sc24 == '8'].index)
    df = df.drop(df[df.sc36 == '8'].index)
    df = df.drop(df[df.sc37 == '8'].index)
    df = df.drop(df[df.sc38 == '8'].index)
    df = df.drop(df[df.sc114 == '4'].index)
    df = df.drop(df[df.sc147 == '8'].index)
    df = df.drop(df[df.sc173 == '8'].index)
    df = df.drop(df[df.sc171 == '8'].index)
    df = df.drop(df[df.sc154 == '8'].index)
    df = df.drop(df[df.sc157 == '8'].index)
    df = df.drop(df[df.sc185 == '8'].index)
    df = df.drop(df[df.sc197 == '8'].index)
    df = df.drop(df[df.sc198 == '8'].index)
    df = df.drop(df[df.sc187 == '8'].index)
    df = df.drop(df[df.sc188 == '8'].index)
    df = df.drop(df[df.sc189 == '8'].index)
    df = df.drop(df[df.sc190 == '8'].index)
    df = df.drop(df[df.sc191 == '8'].index)
    df = df.drop(df[df.sc192 == '8'].index)
    df = df.drop(df[df.sc194 == '8'].index)
    df = df.drop(df[df.sc196 == '8'].index)
    df = df.drop(df[df.sc199 == '8'].index)
    df = df.drop(df[df.sc575 == '8'].index)
    df = df.drop(df[df.rec15 == '10'].index)
    df = df.drop(df[df.rec15 == '12'].index)
    
    
#Create a new dataframe by performing one hot encoding on the remaining columns that contain categorical features
#Save the row of column labels as a separate array
#Delete the "Monthly Contract Rent" label


    cat_var = list(range(0,30)) + [31,33,34,35] + list(range(38,45)) + [47,49,50,51,52] + list(range(54,67)) + [68,69,70,73] 
    df_OHE = pd.get_dummies(df, columns = df.columns[[cat_var]])

    df_labels = df_OHE.columns
    df_labels = df_labels.drop('uf17', 1)
    feature_labels = np.array(df_labels)
    
    
#Convert the dataframe to a Numpy array
#Delete the row of column labels
#Convert entries from string to int
#Remove the "Monthly Contract Rent" column from the feature columns


    housing = df_OHE.as_matrix()

    housing = np.delete(housing, (0), axis=0)
    housing = housing.astype(np.float)

    rent = housing[:,4]
    housing = np.delete(housing, 4, axis=1)

    
#Perform standard scaling and a grid search for the best ridge regression parameter alpha between 1 and 50
#Return the R^2 score achieved using the best alpha value found by grid search
    
    
    X, y = housing, rent
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 5, train_size = .8)
    pipe = Pipeline([('scaler', StandardScaler()),
                    ('ridge', Ridge())])
    
    parameters ={'ridge__alpha': range(1,50)}
    grid = GridSearchCV(pipe, parameters, cv = 10)
    grid.fit(X_train, y_train)

    r = grid.score(X_test, y_test)
    
    return(r)


# In[56]:

def predict_rent():
    """"""
    """"""
    
    
#Download the csv file and store it as a pandas dataframe


    data = urllib.request.urlopen('https://ndownloader.figshare.com/files/7586326')
    f = csv.reader(io.TextIOWrapper(data))
    dataset = list(f)
    df = pd.DataFrame(dataset)
    
    
#Assign row 0 to the be the column names
#Drop the feature columns that are related to occupants and not apartments
#Drop the feature columns that are related to owner occupied properties
#Drop rows for which the "Monthly Contract Rent" column (the response variable) has a missing value
#Drop rows with missing values


    df.columns = df.iloc[0]
    dropped = [0] + list(range(30,44)) + list(range(45,65)) + [89,90,93,94,95,96,97,98,113,114,115,116] + list(
    range(119,124)) + list(range(130,136)) + list(range(140,162)) + list(range(163,197)) + list(range(80,89))

    df = df.drop(df[df.uf17 == '99999'].index)
    df = df.drop(df.columns[[dropped]], axis = 1)
    df = df.drop(df[df.uf1_1 == '8'].index)
    df = df.drop(df[df.uf1_7 == '8'].index)
    df = df.drop(df[df.uf1_12 == '8'].index)
    df = df.drop(df[df.uf1_17 == '8'].index)
    df = df.drop(df[df.sc23 == '8'].index)
    df = df.drop(df[df.sc24 == '8'].index)
    df = df.drop(df[df.sc36 == '8'].index)
    df = df.drop(df[df.sc37 == '8'].index)
    df = df.drop(df[df.sc38 == '8'].index)
    df = df.drop(df[df.sc114 == '4'].index)
    df = df.drop(df[df.sc147 == '8'].index)
    df = df.drop(df[df.sc173 == '8'].index)
    df = df.drop(df[df.sc171 == '8'].index)
    df = df.drop(df[df.sc154 == '8'].index)
    df = df.drop(df[df.sc157 == '8'].index)
    df = df.drop(df[df.sc185 == '8'].index)
    df = df.drop(df[df.sc197 == '8'].index)
    df = df.drop(df[df.sc198 == '8'].index)
    df = df.drop(df[df.sc187 == '8'].index)
    df = df.drop(df[df.sc188 == '8'].index)
    df = df.drop(df[df.sc189 == '8'].index)
    df = df.drop(df[df.sc190 == '8'].index)
    df = df.drop(df[df.sc191 == '8'].index)
    df = df.drop(df[df.sc192 == '8'].index)
    df = df.drop(df[df.sc194 == '8'].index)
    df = df.drop(df[df.sc196 == '8'].index)
    df = df.drop(df[df.sc199 == '8'].index)
    df = df.drop(df[df.sc575 == '8'].index)
    df = df.drop(df[df.rec15 == '10'].index)
    df = df.drop(df[df.rec15 == '12'].index)
    
    
#Create a new dataframe by performing one hot encoding on the remaining columns that contain categorical features
#Save the row of column labels as a separate array
#Delete the "Monthly Contract Rent" label


    cat_var = list(range(0,30)) + [31,33,34,35] + list(range(38,45)) + [47,49,50,51,52] + list(range(54,67)) + [68,69,70,73] 
    df_OHE = pd.get_dummies(df, columns = df.columns[[cat_var]])

    df_labels = df_OHE.columns
    df_labels = df_labels.drop('uf17', 1)
    feature_labels = np.array(df_labels)
    
    
#Convert the dataframe to a Numpy array
#Delete the row of column labels
#Convert entries from string to int
#Remove the "Monthly Contract Rent" column from the feature columns


    housing = df_OHE.as_matrix()

    housing = np.delete(housing, (0), axis=0)
    housing = housing.astype(np.float)

    rent = housing[:,4]
    housing = np.delete(housing, 4, axis=1)

    
#Perform standard scaling and a grid search for the best ridge regression parameter alpha between 1 and 50
#Returns the test data, true labels, and predicted labels used to score the model


    X, y = housing, rent
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state = 5, train_size = .8)

    pipe = Pipeline([('scaler', StandardScaler()),
                    ('ridge', Ridge())])
    parameters ={'ridge__alpha': range(1,50)}
    grid = GridSearchCV(pipe, parameters, cv = 10)
    grid.fit(X_train, y_train)

    test_data = np.vstack((feature_labels, X_test))
    
    return('test data:', test_data, 'true labels:', y_test, 'predicted labels:', grid.predict(X_test))


# In[57]:

score_rent()
predict_rent()

