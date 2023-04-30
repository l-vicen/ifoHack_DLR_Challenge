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
    dataframe_no_labels = load_data(pathTwo)

    # make columns numerical
    non_numeric_cols = ['Area_Types']
    df = pd.get_dummies(dataframe_total, columns=non_numeric_cols)
    df = df.drop(['City_Name', 'Unnamed: 0'], axis = 1)

    df = df.dropna()

    X = df.drop('Land_Value', axis = 1)
    y = df['Land_Value']

    scaler = StandardScaler()
    scaler.fit(X)
    X_normalized = scaler.transform(X)
    # Create a PCA object
    pca = PCA(n_components=10)
    # Fit and transform the data
    X = pca.fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    rf = RandomForestRegressor(n_estimators=100, max_depth=5)
    rf.fit(X_train, y_train)

    return dataframe_total, X, rf

def predictor(fdi, city, total_data_set, no_label_data_set, rf):
    
    try:
        selected_row = total_data_set[(total_data_set['Neighborhood_FID'] == fdi) & (total_data_set['City_Name'] == city)]
        row_index = selected_row.index[0]
        real_price = selected_row["Land_Value"]
        st.write(selected_row)
        st.write(row_index)

        no_label_data_set = pd.DataFrame(no_label_data_set)

        parameters = no_label_data_set.loc[row_index]
        model_suggested_price = rf.predict([parameters])
        return real_price, model_suggested_price

    except:
        return -1.0, -1.0