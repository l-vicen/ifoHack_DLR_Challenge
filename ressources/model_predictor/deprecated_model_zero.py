import pandas as pd
import tensorflow as tf
from tensorflow.keras import layers
import matplotlib.pyplot as plt
from keras.callbacks import EarlyStopping
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics import r2_score
scaler = MinMaxScaler()
import numpy as np

total_df = pd.read_csv("total_df.csv")
total_df = total_df.drop(columns=["Neighborhood_FID", "Unnamed: 0", "City_Name", "Area_Types"]).sample(frac=1)
total_df = total_df[total_df["Land_Value"]<2500].reset_index(drop=True)
print(total_df)
df = total_df.drop(columns=["Land_Value"]).dropna(axis=1)
df = scaler.fit_transform(df)
pca = pd.DataFrame(PCA(n_components=0.95).fit_transform(df))
print(pca)

# K-fold cross validation
r2 = []
for i in range(0, 6):
    model = tf.keras.Sequential([
        layers.Dense(4, activation='relu', input_shape=[21]),
        layers.Dense(8, activation='relu'),
        layers.Dense(4, activation='relu'),
        layers.Dense(1, activation='linear')
    ])
    model.compile(loss='mean_squared_error',
                  optimizer=tf.keras.optimizers.Adam(learning_rate=0.01),
                  metrics=[tf.keras.metrics.RootMeanSquaredError()])
    model.summary()
    early = EarlyStopping(monitor="root_mean_squared_error", min_delta=0, patience=50, verbose=1, mode="auto",
                          restore_best_weights=True)
    X_test = pca.iloc[i*50:(i+1)*50, :]
    y_test = total_df["Land_Value"][i*50:(i+1)*50]
    X_train = pca.drop(range(i*50, (i+1)*50))
    y_train = total_df["Land_Value"].drop(range(i*50, (i+1)*50))
    model.fit(X_train, y_train, epochs=300, batch_size=16, callbacks=[early])
    test_predict = model.predict(X_test)
    score = r2_score(y_test.to_numpy(), test_predict.flatten())
    r2.append(score)

print(np.mean(r2))