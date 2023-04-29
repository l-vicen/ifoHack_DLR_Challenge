# In-house lib
from ressources import StyleHelpers

# 3rd Party lib
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import FunctionTransformer
from sklearn.linear_model import RidgeCV
from sklearn.linear_model import Ridge
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import OneHotEncoder
import plotly.express as px
import plotly.graph_objects as go

# Sidebar Configuration
StyleHelpers.add_dlr_logo_to_page()

# Prediction Model
st.title("Feature Selection")

# Dashboard for the data preprocessing that our team did
# Cache the dataframe so it's only loaded once
@st.cache_data
def load_data():
    return pd.read_csv("data/1 Land Prices/model_data/Berlin_v1.csv")

df = load_data()
df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
st.dataframe(df)

# Feature Selection
list_columns = df.columns.values.tolist()

# X-variables & y-variable
Xs = st.multiselect('Pick the Xs variables: ', list_columns)
y = "Land_Value"

# Model Creation
train, test = train_test_split(df, test_size=0.25, random_state=83)

if (len(Xs) > 0):
    models = {}
    y_predictor = []
    for i in range(len(Xs)):
        features = Xs[:(i+1)]
        name = ",".join([name[0] for name in features])
        # The pipeline for the ith model
        model = Pipeline([
            ("SelectColumns", ColumnTransformer([
                ("keep", "passthrough", features),
            ])),
            ("Imputation", SimpleImputer()),
            ("LinearModel", LinearRegression())
        ])
        # Fit the pipeline
        model.fit(train, train[y]);
        # Saving the ith model
        models[name] = model

    st.write("We are considering model with X-variable tuples: {}".format(models.keys()))

    # Model Cross Validation
    st.title("Model Cross-Validation")

    # Root Mean Square Root Function
    def rmse_score(model, X, y):
        return np.sqrt(np.mean((y - model.predict(X))**2))

    # Applying RMSE in Cross-Validation Sklearn
    feature_tuples = list(models.keys())
    model_performance = [cross_val_score(models[feature_tuples[i]], train, train[y], scoring=rmse_score, cv=5) for i in range(len(feature_tuples))]
    st.write(model_performance)

    # Taking the mean of the cv = 5
    mean_variance_performance = [np.mean(p) for p in model_performance]
    st.write(mean_variance_performance)

    # Ploting model RMSE
    def compare_models(models, train, test, yVar):
        # Compute the training error for each model
        training_rmse = [rmse_score(model, train, train[yVar]) for model in models.values()]
        # Compute the cross validation error for each model
        validation_rmse = [np.mean(cross_val_score(model, train, train[yVar], scoring=rmse_score, cv=5)) 
                        for model in models.values()]
        # Compute the test error for each model (don't do this!)
        test_rmse = [rmse_score(model, test, test[yVar]) for model in models.values()]
        names = list(models.keys())
        fig = go.Figure([
            go.Bar(x = names, y = training_rmse, name="Training RMSE"),
            go.Bar(x = names, y = validation_rmse, name="CV RMSE"),
            go.Bar(x = names, y = test_rmse, name="Test RMSE", opacity=.3)])
        fig.update_yaxes(title="RMSE")
        return fig
    st.plotly_chart(compare_models(models, train, test, "Land_Value"))

    # Ridge Model
    alphas = np.linspace(0.5, 3, 30)

    ridge_model = Pipeline([
        ("SelectColumns", ColumnTransformer([
            ("keep", StandardScaler(), Xs),
            # ("origin_encoder", OneHotEncoder(), ["origin"]),
            # ("text", CountVectorizer(), "name")
        ])),
        ("Imputation", SimpleImputer()),
        ("LinearModel", RidgeCV(alphas=alphas))
    ])

    ridge_model.fit(train, train[y])
    models["RidgeCV"] = ridge_model
    st.plotly_chart(compare_models(models, train, test, "Land_Value"))

# st.title("Descriptive Analysis")
# col1, col2 = st.columns(2)

# def plot_scatter(df, varX, varY):
#     fig_scatter = px.scatter(df, x=varX, y=varY, marginal_x="box", marginal_y="violin")
#     col1.plotly_chart(fig_scatter, theme="streamlit", use_container_width=True)

# if (varX != None and varY != None):
#     plot_scatter(df, varX, varY)