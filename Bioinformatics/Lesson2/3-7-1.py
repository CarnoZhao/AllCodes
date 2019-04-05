from LoadFile import LoadFile
from collections import defaultdict

f = open(LoadFile())
protein = f.readline().rstrip()
f.close()

masstable = defaultdict(int)
f = open('integer_mass_table.txt')
for l in f:
	masstable[l.rstrip().split(' ')[0]] = eval(l.rstrip().split(' ')[1])
f.close()

prefix = [0]
for aa in protein:
	prefix.append(prefix[-1] + masstable[aa])

ret = [0]
for i in range(len(prefix) - 1):
	for j in range(i + 1, len(prefix)):
		ret.append(prefix[j] - prefix[i])
print(' '.join(map(lambda x: str(x), ret)))