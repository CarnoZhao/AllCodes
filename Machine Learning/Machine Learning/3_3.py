import numpy as nppip

def sigmoid(x):
	ret = 1 / (1 + )

with open('3_0_alpha.txt') as f:
	ls = f.read()
	f.close()
ls = ls.split('\n')[1:]
for i in range(len(ls)):
	ls[i] = list(map(lambda x: eval(x), ls[i].split(' ')))
ls = np.array(ls)
X = ls[..., 1:3]
y = ls[..., 3]
