from collections import defaultdict
from copy import deepcopy

weights = set()
f = open('integer_mass_table.txt')
for l in f:
	weights.add(eval(l.rstrip().split(' ')[1]))
f.close()

#target = 1000

def func351(target, weights):
	ret = 0
	masses = defaultdict(int)
	for mass in weights:
		masses[mass] += 1
	while target > min(masses.keys()):
		temp = defaultdict(int)
		for key in masses:
			for mass in weights:
				temp[mass + key] += masses[key]
		masses = deepcopy(temp)
		ret += masses[target]
	return ret

def func532(weights):
	import random
	itertime = 10
	C = 0
	for i in range(itertime):
		m1, m2 = random.randint(1000, 3000), random.randint(1000, 3000)
		N1, N2 = func351(m1, weights), func351(m2, weights)
		C += (N1 / N2) ** (1 / (m1 - m2))
	C /= itertime
	return C

C = func532(weights)
print(C)