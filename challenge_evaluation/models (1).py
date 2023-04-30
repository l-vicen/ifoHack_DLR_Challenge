def model_fit(X_train, y_train):
    rf = RandomForestRegressor(n_estimators=100, max_depth=5)
    rf.fit(X_train, y_train)
    return rf

def model_predict(rf, X_test):
    y_pred = rf.predict(X_test)
    return y_pred