def mis_count(pattern, part):
	cnt = 0
	for i in range(l):
		if pattern[i] != part[i]:
			cnt += 1
	return cnt

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

with open('D:/Browser Download/dataset_9_8 (1).txt') as f:
	text = f.readline().rstrip()
	l, k = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
	f.close()
ret = []
maxcnt = 0
for j in range(len(text) - l + 1):
	pattern = text[j: j + l]
	pattern_rc = r_c(pattern)
	cnt = 0
	for i in range(len(text) - l + 1):
		part = text[i: i + l]
		if mis_count(pattern, part) <= k:
			cnt += 1
		if mis_count(pattern_rc, part) <=k:
			cnt += 1
	if cnt > maxcnt:
		ret = [pattern, r_c(pattern)]
		maxcnt = cnt
	elif cnt == maxcnt and pattern not in ret:
		ret.extend([pattern, r_c(pattern)])
print(' '.join(ret))