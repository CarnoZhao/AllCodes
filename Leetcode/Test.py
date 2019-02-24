import numpy as np
from itertools import combinations
energy = lambda x1, x2, x3: 'energy'
n = 5
z = np.array([list(x) + [energy(x[0], x[1], x[2])] for x in combinations([i for i in range(1, n + 1) for j in range(3)], 3)])
for line in z:
	print('\t'.join(line.tolist()))