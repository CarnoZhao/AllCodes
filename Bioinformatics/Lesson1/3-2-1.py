def get_fname(path):
	import os
	filelist = os.listdir(path)
	maxtime = 0
	for file in filelist:
		time = os.stat(path + file).st_mtime
		if time > maxtime:
			fname = file
			maxtime = time
	return fname

def text_mis_count(pattern, text, k, d):
	find = False
	for i in range(len(text) - k + 1):
		part = text[i: i + k]
		cnt = 0
		for j in range(k):
			if part[j] != pattern[j]:
				cnt += 1
		if cnt <= d:
			find = True
			break
	return find

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

def main():
	ret = []
	dna = []
	path = 'D:/Browser Download/'
	fname = get_fname(path) #156_8
	f = open(path + fname)
	(k, d) = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
	for l in f:
		dna.append(l.rstrip())
	f.close()
	kmerset = [number_to_pattern(number, k) for number in range(4**k)]
	for kmer in kmerset:
		find = True
		for text in dna:
			if not text_mis_count(kmer, text, k, d):
				find = False
				break
		if find != False:
			ret.append(kmer)
	print(' '.join(ret))

main()