import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('pima-indians-diabetes3.csv')

data = data.dropna()

y데이터 = data['diabetes'].values

x데이터 = data.iloc[:, 0:8].values.tolist()


model = tf.keras.models.Sequential([
    tf.keras.layers.Dense(64, activation='tanh'),
    tf.keras.layers.Dense(128, activation='tanh'),
    tf.keras.layers.Dense(1, activation='sigmoid'),
])

model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'] )

model.fit( np.array(x데이터), np.array(y데이터), epochs=1000 )

