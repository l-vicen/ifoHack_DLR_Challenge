import pandas as pd
import streamlit as st
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA

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

    # make columns numerical
    non_numeric_cols = ['Area_Types']
    df = pd.get_dummies(dataframe_total, columns=non_numeric_cols)
    df = df.drop(['City_Name', 'Unnamed: 0'], axis = 1)
    df = df.dropna()

    X = df.drop('Land_Value', axis = 1)
    y = df['Land_Value']

    # Create a PCA object
    pca = PCA(n_components=10)
    # Fit and transform the data
    X = pca.fit_transform(X)
    
    rf = RandomForestRegressor(n_estimators=100, max_depth=5)
    rf.fit(X, y)

    return dataframe_total, pca, rf

def predictor(fdi, city, total_data_set, pca, rf):
    
    try:
        selected_row = total_data_set[(total_data_set['Neighborhood_FID'] == fdi) & (total_data_set['City_Name'] == city)]
        # st.write(selected_row)
        
        row_index = selected_row.index[0]
        # st.write(row_index)

        real_price = selected_row["Land_Value"]
        # st.write(real_price)
        
        non_numeric_cols = ['Area_Types']
        df = pd.get_dummies(total_data_set, columns=non_numeric_cols)
        df = df.drop(['City_Name', 'Unnamed: 0'], axis = 1)
        df = df.dropna()
  
        X = df.drop('Land_Value', axis = 1)
        # st.write(X)

        parameters = X.loc[row_index]
        # st.write(parameters)                
                                        
        parameters = pca.transform([parameters])
        # st.write(parameters)  

        model_suggested_price = rf.predict(parameters)
        # st.write(model_suggested_price)

        return real_price, model_suggested_price

    except:
        return -1.0, -1.0