from LoadFile import LoadFile

def makeSpec(peptide, weights):
	pass

f = open('integer_mass_table.txt')
weights = list({eval(l.rstrip().split(' ')[1]) for l in f})

f = open(LoadFile())
spec = list(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
f.close()

singlepep = list(filter(lambda x: x in spec, weights))
peps = [[0]]
newspecmax = 0
#initialize

while newspecmax != max(spec):
	for pep in peps:
		for aa in singlepep:
			fit = 1
			for i in range(len(pep)):
				if sum(pep[-i - 1:] + [aa]) not in spec:
					fit = 0
					break
			if fit != 0:
				peps.append(pep + [aa])
	newspecmax = max([sum(pep) for pep in peps])
print('\n'.join(['-'.join(list(map(lambda x: str(x), pep[1:]))) for pep in filter(lambda x: sum(x) == max(spec), peps)]))