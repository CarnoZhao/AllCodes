def filename(path):
	import os
	return os.listdir(path)[list(map(lambda x: os.stat(path + x).st_mtime, os.listdir(path))).index(max(list(map(lambda x: os.stat(path + x).st_mtime, os.listdir(path)))))]

def loadfile(fname):
	f = open(fname)
	k = eval(f.readline().rstrip())
	dnas = []
	for l in f:
		dnas.append(l.rstrip())
	f.close()
	return k, dnas

def number_to_pattern(number, k):
	i = k
	ref = 'ACGT'
	ret = [0] * k
	while number != 0:
		if number - 4 ** (i - 1) >= 0:
			number -= 4 ** (i - 1)
			ret[i - 1] += 1
		else:
			i -= 1
	s = ''
	for idx in ret:
		s += ref[idx]
	return s[::-1]

def ham_d_s(kmer, dnas):
	ret = 0
	for dna in dnas:
		ret += ham_d(kmer, dna)
	return ret

def ham_d(kmer, dna):
	mind = len(dna)
	for i in range(len(dna) - len(kmer) + 1):
		part = dna[i: i + len(kmer)]
		cnt = 0
		for x, y in zip(part, kmer):
			cnt = cnt + 1 if x != y else cnt
		mind = cnt if cnt < mind else mind
	return mind

def main():
	path = 'D:/Browser Download/'
	fname = path + filename(path)
	k, dnas  = loadfile(fname)
	minsumd = len(dnas) * len(dnas[0])
	ret = ''
	for kmer in [number_to_pattern(number, k) for number in range(4**k)]:
		hamd = ham_d_s(kmer, dnas)
		if hamd < minsumd:
			minsumd = hamd
			ret = kmer
	print(ret)

main()