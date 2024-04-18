import tensorflow as tf
import numpy as np
import pandas as pd

data = pd.read_csv('pima-indians-diabetes3.csv')

data = data.dropna()

