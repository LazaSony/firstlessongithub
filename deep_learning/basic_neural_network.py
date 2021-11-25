from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
import numpy as np
# import matplotlib.pyplot as plt
# %matplotlib inline

# Generate dataset
trX = np.linspace(-1, 1, 101)
trY = 2 * trX + np.random.randn(*trX.shape) * 0.33 # create a y value which is approximately linear but with some random noise