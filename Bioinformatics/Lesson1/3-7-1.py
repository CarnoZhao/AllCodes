def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	f = open(filename)
	kmer = f.readline().rstrip()
	dnas = f.readline().rstrip().split(' ')
	return kmer, dnas

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
	filename = file_name(path)
	kmer, dnas = load_file(filename)
	print(ham_d_s(kmer, dnas))

main()