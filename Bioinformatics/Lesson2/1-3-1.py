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
	for i, kmer in enumerate(kmers):
		if i == 0:
			ret = kmers[i]
		else:
			ret += kmers[i][-1]
	print(ret)

main()