import matplotlib.pyplot as plt

def find_minGC(fname):
	with open(fname) as f:
		f.readline()
		cnt = [0]
		for line in f:
			line = line.rstrip()
			for pos in line:
				if pos == 'C':
					cnt.append(cnt[-1] - 1)
				elif pos == 'G':
					cnt.append(cnt[-1] + 1)
				else:
					cnt.append(cnt[-1])
		f.close()
	return cnt.index(min(cnt))

def cutout_ori(fname, minidx, window_lenth):
	with open(fname) as f:
		f.readline()
		lenth = len(f.readline().rstrip())
		x = (minidx - window_lenth) // lenth + 1
		y = (minidx + window_lenth) // lenth + 1
		ori_text = ''
		cnt = 1
		for line in f:
			if cnt == x:
				ori_text += line.rstrip()[minidx - window_lenth - x * lenth:]
			elif cnt > x and cnt < y:
				ori_text += line.rstrip()
			elif cnt == y:
				ori_text += line.rstrip()[:minidx + window_lenth - (y - 1) * lenth]
				break
			cnt += 1
		f.close()
	return ori_text

def r_c(pattern):
	ret = ''
	for c in pattern:
		if c == 'A':
			ret += 'T'
		elif c == 'C':
			ret += 'G'
		elif c == 'G':
			ret += 'C'
		elif c == 'T':
			ret += 'A'
	ret = ret[::-1]
	return ret

def mis_count(kmer, part):
	cnt = 0
	for i in range(len(kmer)):
		if kmer[i] != part[i]:
			cnt += 1
	return cnt

def most_frequent_kmer(ori, k, mismatch_tolerance):
	ret = []
	maxcnt = 0
	for i in range(len(ori) - k + 1):
		kmer = ori[i: i + k]
		cnt = 0
		for j in range(len(ori) - k + 1):
			part = ori[j: j + k]
			if mis_count(kmer, part) <= mismatch_tolerance:
				cnt += 1
			if mis_count(r_c(kmer), part) <= mismatch_tolerance:
				cnt += 1
		if cnt > maxcnt:
			ret = [(kmer, r_c(kmer))]
			maxcnt = cnt
		elif cnt == maxcnt and (kmer, r_c(kmer)) not in ret:
			ret.append((kmer, r_c(kmer)))
	return ret, maxcnt

def main():
	window_lenth = 500
	mismatch_tolerance = 1
	kmer_range = range(4, 11)
	minidx = find_minGC('Salmonella_enterica.txt')
	text = cutout_ori('Salmonella_enterica.txt', minidx, window_lenth)
	kmer_set = {}
	for k in kmer_range:
		kmer_set[k] = most_frequent_kmer(text, k, mismatch_tolerance)
	ratio = [x[1] * 4**k / (2 * window_lenth) for x, k in zip(list(kmer_set.values()), kmer_range)]
	opti_k = min(kmer_range) + ratio.index(max(ratio))
	result = kmer_set[opti_k]
	print(result)
	print("The most frequent k-mer (considering its length) is:")
	print("\t   k-mer = %s," % result[0][0][0])
	print("\trc-k-mer = %s," % result[0][0][1])
	print("which appeared %d times." % result[1])
	'''fig = plt.subplot(111)
	plt.plot(kmer_range, ratio, label = 'Ratio')
	plt.legend()
	plt.show()'''

main()