def pattern_to_number(pattern, k):
	ret = 0
	for c in pattern:
		idx = 'ACGT'.index(c)
		ret += idx * 4 ** (k - 1)
		k -= 1
	return ret

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

def window_count(window, k, L):
	ls = [0] * 4 ** k
	for i in range(L - k + 1):
		pattern = text[i: i + k]
		indx = pattern_to_number(pattern, k)
		ls[indx] += 1
	return ls

def main_1():
	with open('data.txt') as f:
		text = f.readline().rstrip()
		#(k, L, t) = tuple(map(lambda x: eval(x), f.readline().rstrip().split(' ')))
		(k, L, t) = (9, 500, 3)
	window = text[:L]
	ret = []
	cntls = window_count(window, k, L)
	for indx in cntls:
		if indx == t:
			ret.append(indx)
	for i in range(len(text) - L + 1):
		idx1 = pattern_to_number(text[i: i + k], k)
		idx2 = pattern_to_number(text[i + L + 1 - k: i + L + 1], k)
		cntls[idx1] -= 1
		cntls[idx2] += 1
		if cntls[idx1] == t and idx1 not in ret:
			ret.append(idx1)
		if cntls[idx2] == t and idx2 not in ret:
			ret.append(idx2)
	ls = list(map(lambda x: number_to_pattern(x, k), ret))
	print(' '.join(ls))
	print(len(ret))

number = 6757
k = 11
print(number_to_pattern(number, k))