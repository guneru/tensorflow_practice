import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('pima-indians-diabetes3.csv')

data = data.dropna()

y데이터 = data['diabetes'].values

x데이터 = [ ]

for i, rows in data.iterrows():
    x데이터.append([ rows['pregnant'], rows['plasma'], rows['pressure'], rows['thickness'], rows['insulin'], rows['bmi'], rows['pedigree'], rows['age'] ])