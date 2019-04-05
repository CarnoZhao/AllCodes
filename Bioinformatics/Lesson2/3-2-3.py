from LoadFile import LoadFile
from collections import defaultdict

def recursion(protein, dnas, codons):
	if len(protein) > 0:
		temp = []
		for codon in codons[protein.pop()]:
			for dna in dnas:
				temp.append(codon + dna)
		dnas = recursion(protein, temp[:], codons)
	return dnas

def r_c(dna):
	ret = ''
	for nt in dna:
		if nt == 'A':
			ret += 'U'
		elif nt == 'C':
			ret += 'G'
		elif nt == 'G':
			ret += 'C'
		else:
			ret += 'A'
	return ret[::-1]

filename = LoadFile()
f = open(filename)
dna = f.readline().rstrip()
protein = f.readline().rstrip()

codons = defaultdict(list)
f = open('Codon.txt')
for l in f:
	l = l.rstrip().split(' ')
	if len(l) == 1:
		codons[''].append(l[0])
	else:
		codons[l[1]].append(l[0])

dnas = ['']
dnas = recursion(list(protein), dnas, codons)
lenth = len(dnas[0])

ret = []
for i in range(len(dna) - lenth):
	substring = dna[i:i + lenth]
	if substring.replace('T', 'U') in dnas or r_c(substring) in dnas:
		ret.append(substring)

print('\n'.join(ret))