import pandas as pd
import numpy as np

s = pd.Series([10, 20, 30 , 40])

print(s)

df = pd.DataFrame({
    'Nombre': ['Ana', 'Luis', 'Maria', 'David'],
    'Edad': [23, 30, 27, 14],
    'Ciudad': ['Bogotá', 'Medellin', 'Cali', 'Bucaramanga'],
})

print(df.head(2))