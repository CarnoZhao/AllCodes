from collections import defaultdict

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

def translate(dna):
	protein = ''
	for i in range(0, len(dna) - 2, 3):
		protein += codons[dna[i: i + 3]]
	return protein

codons = defaultdict(str)
f = open('Codon.txt')
for l in f:
	l = l.rstrip().split(' ')
	codons[l[0]] = l[1] if len(l) != 1 else ''
protein = 'VKLFPWFNQY'
f.close()

row = 0
f = open('Bacillus_brevis.txt')
for l in f:
	row += 1
f.close()

cnt, preline, nowrow, lenth = 0, '', 0, len(protein) * 3
f = open('Bacillus_brevis.txt')
for l in f:
	nowrow += 1
	print('File has been read: %.3f%%' % (100 * nowrow / row))
	print('cnt = %d' % cnt)
	print('\n' * 6)
	dna = preline + l
	for i in range(len(dna) - lenth):
		substring = dna[i:i + lenth]
		if translate(substring) == protein or translate(r_c(substring)) == protein:
			cnt += 1
	preline = dna[-lenth + 1:]
f.close()
print('File has been read: %.3f%%' % (100 * nowrow / row))
print('cnt = %d' % cnt)
print('\n' * 6)