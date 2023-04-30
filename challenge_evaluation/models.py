from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.decomposition import PCA
import pandas as pd

def model_fit(X_train, y_train):
    rf = RandomForestRegressor(n_estimators=100, max_depth=5)
    rf.fit(X_train, y_train)
    return rf

def model_predict(rf, X_test):
    y_pred = rf.predict(X_test)
    return y_pred