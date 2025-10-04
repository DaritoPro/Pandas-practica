import pandas as pd
import numpy as np

df = pd.read_csv('archive/all_data.csv', index_col=0)

print(df.head())