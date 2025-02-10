import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load data
data = pd.read_csv('btc_1h_data_2018_to_2025.csv')

data = data[20000:30000]

# save data
data.to_csv('data.csv', index=False)