import numpy as np
data = []
with open('FilterData.txt') as f:
	for l in f:
		line = l.rstrip().split(',')
		data.append(line)
data = np.array(data)
kinds = np.zeros((np.size(data, 1), 1))
for c in range(np.size(data, 1)):
	cnt = 0
	try:
		val = eval(data[0, c])
		continue
	except:
		sets = set(data[..., c])
		kinds[c] = len(sets)
print(kinds)