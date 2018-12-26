from LoadFile import LoadFile
from collections import defaultdict

fn = LoadFile()
f = open(fn)
protein = f.readline().rstrip()
f.close()

weights = defaultdict(int)
f = open('integer_mass_table.txt')
for l in f:
	weights[l.rstrip().split(' ')[0]] = eval(l.rstrip().split(' ')[1])
f.close()

masses = [0]
masses.append(sum([weights[aa] for aa in protein]))
for lenth in range(1, len(protein)):
	mass = sum([weights[aa] for aa in protein[:lenth]])
	for i in range(len(protein)):
		mass += weights[protein[(lenth + i) % len(protein)]] - weights[protein[i]]
		masses.append(mass)
print(' '.join([str(x) for x in sorted(masses)]))