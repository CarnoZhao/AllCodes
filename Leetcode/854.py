def ClearSame(A, B):
	i = 0
	cnt = 0
	while i < len(A):
		if A[i] == B[i]:
			cnt += 1
			del A[i], B[i]
		else:
			i += 1
	return A, B, cnt

def FindMax1(ABlist):
	ret = []
	match = 0
	for A, B in ABlist:
		for i in range(len(A) - 1):
			for j in range(i, len(A)):
				temp = A[:]
				temp[i], temp[j] = temp[j], temp[i]
				tempB = B[:]
				tempA, tempB, cnt = ClearSame(temp, tempB)
				if tempA == tempB:
					match = 1
					print(len(ret), 1)
					return ret, match
				if cnt == 2:
					print(len(ret), 2)
					return [[tempA, tempB]], match
				elif cnt == 1:
					ret.append([tempA, tempB])
	print(len(ret), 3)
	return ret, match

def FindMax2(ABlist):
	maxsimi = 0
	ret = []
	match = 0
	for A, B in ABlist:
		for i in range(len(A) - 1):
			for j in range(i, len(A)):
				temp = A[:]
				temp[i], temp[j] = temp[j], temp[i]
				tempB = B[:]
				tempA, tempB, cnt = ClearSame(temp, tempB)
				if tempA == tempB:
					match = 1
					print(len(ret), 1)
					return ret, match
				if cnt > maxsimi:
					ret = [[tempA, tempB]]
					maxsimi = cnt
					print(2)
				elif cnt == maxsimi:
					ret.append([tempA, tempB])
	print(len(ret), 3)
	return ret, match

def main():
	A, B= "abcdefabcdefabcdef", "acccafdeaddbbefbef"
	A, B = list(A), list(B)
	cnt = 0
	A, B, simi = ClearSame(A, B)
	ABlist = [[A, B]]
	match = 0 if A != B else 1
	while match == 0:
		ABlist, match = FindMax1(ABlist)
		cnt += 1
	print(cnt)

main()
