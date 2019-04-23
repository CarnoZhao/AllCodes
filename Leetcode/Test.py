import random 
import pandas as pd
import numpy as np

name = [random.choice('ACGT') for _ in range(100)]
value = [random.randint(-1000, 1000) for _ in range(100)]

df = pd.read_table('/mnt/d/Tencent/Files/gene_Psi.txt')
df.columns = ['name', 'value']
df.value.apply(eval)
print(df.groupby('name')['value'].apply(lambda x: max(abs(x)) * (1 if max(abs(x)) in x.tolist() else -1)))

