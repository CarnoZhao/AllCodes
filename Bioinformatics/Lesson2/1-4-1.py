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
	return k, dna

def main():
	path = 'D:/Browser Download/'
	filename = file_name(path)
	k, dna = load_file(filename)
	fw = open('ret.txt', 'w')
	ret = {}
	for i in range(len(dna) - k + 1):
		part = dna[i: i + k]
		if part[:-1] in ret:
			ret[part[:-1]].append(part[1:])
		else:
			ret[part[:-1]] = [part[1:]]
	for part in ret:
		fw.write('%s -> %s\n' % (part, ','.join(ret[part])))
	fw.close()

main()