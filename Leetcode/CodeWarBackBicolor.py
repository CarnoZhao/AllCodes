from itertools import combinations
from math import ceil
from collections import defaultdict

def multi2(N, m):
    N2 = N
    a = list(range(m, N + m))
    while N2 > 1:
        N1 = N2 % 2; N2 = N2 // 2 + N1
        for i in range(N2 - N1):
            a[i] *= a[N2 + i]
        a = a[0: N2]
    return a[0]

def C(m, n):
	ret = multi2(n, m - n + 1) // multi2(n, 1)
	return ret % 12345787

def makeList(r, g, b, number):
	ret = defaultdict(list)
	for colors in combinations([r, g, b], 2):
		c1, c2 = colors
		for n in range(0, number):
			cnt = 0
			for num1 in range(1, n // c1 + 1):
				for num2 in range(1, n // c2 + 1):
					if n - c1 * num1 - c2 * num2 < 0:
						continue
					bnum = C(n - c1 * num1 - c2 * num2 + num1 + num2, num1 + num2)
					cnum = C(num1 + num2, num1)
					cnt += bnum * cnum
			ret[colors].append(cnt)
	return ret

def Function(n, r, g, b):
	cnt = 0
	for colors in combinations([r, g, b], 2):
		c1, c2 = colors
		for num1 in range(1, n // c1 + 1):
			for num2 in range(1, n // c2 + 1):
				if n - c1 * num1 - c2 * num2 < 0:
					continue
				bnum = C(n - c1 * num1 - c2 * num2 + num1 + num2, num1 + num2) % 12345787
				cnum = C(num1 + num2, num1) % 12345787
				cnt += bnum * cnum
	return cnt % 12345787

def insane_tri_bicolor_tiling(n, r, g, b):
	'''number = 30
	chooseList = makeList(r, g, b, number)
	cnt = 0
	for cs in combinations([r, g, b], 2):
		cnt += f(n, cs, number, chooseList)
	return cnt % 12345787'''
	return Function(n, r, g, b)

print(insane_tri_bicolor_tiling(100, 2, 3, 4))