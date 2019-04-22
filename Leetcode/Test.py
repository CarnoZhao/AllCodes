import random 
import pandas as pd
import numpy as np

name = [random.choice('ACGT') for _ in range(100)]
value = [random.randint(-100, 1000) for _ in range(100)]

df = pd.DataFrame({'name':name, 'value':value})
print(df['value'].argmax)
# print(df.groupby('name')['value'].apply(lambda x: max(abs(x)) * (1 if max(abs(x)) in x['value'] else -1)))

