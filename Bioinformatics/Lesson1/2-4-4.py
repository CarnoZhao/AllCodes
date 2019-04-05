def mis_count(pattern, part):
	cnt = 0
	for i in range(l):
		if pattern[i] != part[i]:
			cnt += 1
	return cnt

with open('D:/Browser Download/dataset_9_7 (1).txt') as f:
	text = f.readline().rstrip()
	l, k = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
	f.close()
ret = []
maxcnt = 0
for j in range(len(text) - l + 1):
	pattern = text[j: j + l]
	cnt = 0
	for i in range(len(text) - l + 1):
		part = text[i: i + l]
		if mis_count(pattern, part) <= k:
			cnt += 1
	if cnt > maxcnt:
		ret = [pattern]
		maxcnt = cnt
	elif cnt == maxcnt and pattern not in ret:
		ret.append(pattern)
print(' '.join(ret))