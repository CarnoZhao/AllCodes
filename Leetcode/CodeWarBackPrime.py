from math import sqrt
def is_prime(n):
	thresh = int(sqrt(n)) + 2
	ret = True
	for i in range(2, thresh):
		if n % i == 0:
			ret = False
			break
	return ret

def re(n):
	string = str(n)[::-1]
	ret = []
	for i in range(len(string)):
		if string[i] == '0':
			continue
		else:
			break
	for j in range(i, len(string)):
		ret.append(string[j])
	return eval(''.join(ret))

def backwardsPrime(start, stop):
	ret = []
	for n in range(start, stop + 1):
		re_n = re(n)
		if is_prime(n) and is_prime(re_n) and n != re_n:
			ret.append(n)
	return ret

print(backwardsPrime(9900, 10000))