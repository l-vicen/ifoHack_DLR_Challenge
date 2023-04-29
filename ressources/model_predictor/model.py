import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def apply_predictor(fdi):

    # Dashboard for the data preprocessing that our team did
    # Cache the dataframe so it's only loaded once
    @st.cache_data
    def load_data():
        return pd.read_csv(r"data/Berlin_v4.csv")

    df = load_data()
    df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
    # st.dataframe(df)

    #--------------------------------------------
    # Calculate the variance of each column
    variances = df.var()
    # Define the variance threshold (e.g., 0.01)
    var_threshold = 0.1
    # Find the constant or almost constant columns
    const_cols = variances[variances <= var_threshold].index
    # Remove the constant or almost constant columns from the dataframe
    df = df.drop(const_cols, axis=1)
    #correlation analysis
    #--------------------------------------------
    correlations = df.corr()['Land_Value'].drop('Land_Value')
    selected_cols = correlations[correlations > 0.62].index.tolist()
    X = df[selected_cols]
    y = df['Land_Value']

    #Model Training
    #--------------------------------------------
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=40)
    model = LinearRegression()
    model.fit(X_train, y_train)
    model.predict(X_test)
    row = [X.iloc[fdi].to_numpy()] 
    return y.iloc[fdi], model.predict(row)