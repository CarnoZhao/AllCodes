def decomSquare(n, maxn):
	sq = int(n ** 0.5)
	if sq **  2 == n and sq < maxn:
		return [sq]
	for i in range(sq - 1, 0, -1):
		ret = decomSquare(n - i ** 2, maxn)
		if ret and ret[-1] < i:
			return ret + [i]
	else:
		return None

def decompose(n):
	return decomSquare(n ** 2, n)
	# your code

print(decompose(8))
