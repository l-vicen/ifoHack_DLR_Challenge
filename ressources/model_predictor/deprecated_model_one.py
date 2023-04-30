import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def preprocessing():

    # Dashboard for the data preprocessing that our team did
    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data(path):
        return pd.read_csv(path)
    
    # Two different datasets containing all cities and features we have collected
    pathOne = "data/total_df.csv"
    pathTwo = "data/Total_No_Land_Values.csv"

    dataframe_total = load_data(pathOne) # Used for training
    dataframe_no_labels = load_data(pathTwo)

    # make columns numerical
    non_numeric_cols = ['Area_Types']
    df = pd.get_dummies(dataframe_total, columns=non_numeric_cols)
    df = df.drop(['City_Name', 'Unnamed: 0'], axis = 1)

    #Drop constant columns
    #--------------------------------------------
    # Calculate the variance of each column
    variances = df.var()
    # Define the variance threshold (e.g., 0.01)
    var_threshold = 0.05
    # Find the constant or almost constant columns
    const_cols = variances[variances <= var_threshold].index
    # Remove the constant or almost constant columns from the dataframe
    df = df.drop(const_cols, axis=1)
    #correlation analysis
    #--------------------------------------------
    correlations = df.corr()['Land_Value'].drop('Land_Value')
    selected_cols = correlations[correlations > 0.5].index.tolist()
    X = df[selected_cols]
    y = df['Land_Value']
    #Model: Linear Regression
    #--------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)

    return dataframe_total, dataframe_no_labels, selected_cols, model

def predictor(fdi, city, total_data_set, no_label_data_set, selected_columns, model):
    selected_row = total_data_set[(total_data_set['Neighborhood_FID'] == fdi) & (total_data_set['City_Name'] == city)]
    row_index = selected_row.index[0]
    real_price = selected_row["Land_Value"]

    parameters = no_label_data_set.loc[row_index][selected_columns]
    model_suggested_price = model.predict([parameters])
    
    return real_price, model_suggested_price