def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	f = open(filename)
	kmers = []
	for l in f:
		kmers.append(l.rstrip())
	f.close()
	return kmers

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	kmers = load_file(filename)
	ret = {}
	for kmer in kmers:
		if kmer[:-1] not in ret:
			ret[kmer[:-1]] = [kmer[1:]]
		else:
			ret[kmer[:-1]].append(kmer[1:])
	fw = open('ret.txt', 'w')
	for kmer in ret:
		fw.write("%s -> %s\n" % (kmer, ','.join(ret[kmer])))
	fw.close()

main()