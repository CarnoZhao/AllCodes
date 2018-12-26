from LoadFile import LoadFile
from collections import defaultdict

f = open(LoadFile())
protein = f.readline().rstrip()
e_spec = list(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
f.close()

#Example
#protein = 'NQEL'
#e_spec = [0, 99, 113, 114, 128, 227, 257, 299, 355, 356, 370, 371, 484]

f = open('integer_mass_table.txt')
masstable = defaultdict(int)
for l in f:
	masstable[l.rstrip().split(' ')[0]] = eval(l.rstrip().split(' ')[1])
f.close()

prefix = [0]
for aa in protein:
	prefix.append(masstable[aa] + prefix[-1])
t_spec = [0]
for i in range(len(prefix)):
	for j in range(i + 1, len(prefix)):
		t_spec.append(prefix[j] - prefix[i])
		'''if i != 0 and j != len(prefix) - 1:#for cycle peptide
			t_spec.append(prefix[-1] - prefix[j] + prefix[i])'''
del prefix

ret = 0
for pep in set(t_spec):
	ret += min(t_spec.count(pep), e_spec.count(pep))
print(ret)