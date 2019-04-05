def mis_count(pattern, part):
	cnt = 0
	for i in range(len(pattern)):
		if pattern[i] != part[i]:
			cnt += 1
	return cnt

with open('D:/Browser Download/dataset_9_6.txt') as f:
	pattern = f.readline().rstrip()
	text = f.readline().rstrip()
	k = eval(f.readline().rstrip())
	f.close()
ret = 0
for i in range(len(text) - len(pattern) + 1):
	part = text[i: i + len(pattern)]
	if mis_count(pattern, part) <= k:
		ret += 1
print(ret)