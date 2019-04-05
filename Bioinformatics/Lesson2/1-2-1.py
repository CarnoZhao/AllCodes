def file_name(path):
	import os
	filelist = os.listdir(path)
	timelist = list(map(lambda x: os.stat(path + x).st_mtime, filelist))
	filename = filelist[timelist.index(max(timelist))]
	return path + filename

def load_file(filename):
	f = open(filename)
	k = eval(f.readline().rstrip())
	dna = f.readline().rstrip()
	f.close()
	return k, dna

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, dna = load_file(filename)
	ret = []
	for i in range(len(dna) - k + 1):
		ret.append(dna[i: i + k])
	ret.sort()
	fw = open('ret.txt', 'w')
	fw.write('\n'.join(ret))
	fw.close()

main()