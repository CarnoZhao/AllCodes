#Preparation with linux code can be found on the book
#This python code is only a part of P93 recipe
def get_non_auto_SNPs(map_file, exclude_file):
	f = open(map_file)
	w = open(exclude_file, 'w')
	for l in f:
		toks = l.rstrip().split('\t')
		chrom = int(toks[0])
		rs = toks[1]
		if chrom > 22:
			w.write('%s/n' % rs)
	w.close()
get_non_auto_SNPs('hapmap10.map', 'exclude10.txt')
get_non_auto_SNPs('hapmap1.map', 'exclude1.txt')