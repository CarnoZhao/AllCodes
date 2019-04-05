from collections import defaultdict
import os


path = 'D:/Browser Download/'
filelist = os.listdir(path)
timelist = [os.stat(path + x).st_mtime for x in filelist]
filename = filelist[timelist.index(max(timelist))]
filename = path + filename
#filename = '4-1-Sample.txt'
pairs = []
f = open(filename)
kmers = [l.rstrip() for l in f]
f.close()

nodes = defaultdict(list)
for kmer in kmers:
	nodes[kmer[:-1]].append(kmer[1:])
del kmer, kmers, filename
#make nodes dictionary

cntin = defaultdict(int)
cntout = defaultdict(int)
for key in nodes:
	cntout[key] += len(nodes[key])
	for value in nodes[key]:
		cntin[value] += 1
#count the in and out route

ret = []
for key in nodes:
	if cntin[key] != 1 or cntout[key] != 1:
		for nextnode in nodes[key]:
			string = key
			while cntin[nextnode] == 1 and cntout[nextnode] == 1:
				string += nextnode[-1]
				nextnode = nodes[nextnode][0]
			string += nextnode[-1]
			ret.append(string)
print(' '.join(sorted(ret)))
print(' '.join(sorted('AGA ATG ATG CAT GAT TGGA TGT'.split(' '))))