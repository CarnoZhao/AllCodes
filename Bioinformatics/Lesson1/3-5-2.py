def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	return filelist[timelist.index(max(timelist))]

def load_file(filename):
	f = open(filename)
	profile = []
	text = f.readline().rstrip()
	k = eval(f.readline().rstrip())
	for l in f:
		profile.append(list(map(lambda x: eval(x), l.rstrip().split(' '))))
	return text, k, profile

def find_kmer(text, k, profile):
	maxpr = 0
	for i in range(len(text) - k + 1):
		part = text[i: i + k]
		pr = 1
		for i, nt in enumerate(part):
			j = 'ACGT'.index(nt)
			pr *= profile[j][i]
		if pr > maxpr:
			maxpr = pr
			ret = part
	return ret

def main():
	path = 'D:/Browser Download/'
	filename = path + file_name(path)
	text, k, profile = load_file(filename)
	result = find_kmer(text, k, profile)
	print(result)

main()