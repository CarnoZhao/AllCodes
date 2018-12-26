from LoadFile import LoadFile
from collections import defaultdict

filename = LoadFile()
with open(filename) as f:
	dna = f.readline().rstrip()
f.close()

codons = defaultdict(str)
with open('Codon.txt') as f:
	for l in f:
		l = l.rstrip().split(' ')
		codons[l[0]] = '' if len(l) == 1 else l[1]

pr = ''
for i in range(0, len(dna) - 2, 3):
	pr += codons[dna[i:i + 3]]
print(pr)