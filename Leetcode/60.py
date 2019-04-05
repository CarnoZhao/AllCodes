n = 4
k = 6
from math import factorial
ret = ''
ls = list(range(1, n + 1))
k -= 1
while n > 0:
	n -= 1
	idx = k // factorial(n) if n > 1 else max(k, 0)
	ret += str(ls[idx])
	del ls[idx]
	k %= factorial(n)
#return ret
print(ret)