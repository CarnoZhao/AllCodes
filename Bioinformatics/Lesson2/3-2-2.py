def recursion(protein, dnas, codons):
	if len(protein) != 0:
		temp = []
		for codon in codons[protein.pop()]:
			for dna in dnas:
				temp.append(codon + dna)
		dnas = recursion(protein, temp[:], codons)
	return dnas

from collections import defaultdict

def main():
	codons = defaultdict(list)
	with open('Codon.txt') as f:
		for l in f:
			l = l.rstrip().split(' ')
			if len(l) != 1:
				codons[l[1]].append(l[0])
			else:
				codons[''].append(l[0])
	protein = 'VKLFPWFNQY'
	dnas = ['']
	dnas = recursion(list(protein), dnas, codons)
	print(dnas)
	print(len(dnas))

main()