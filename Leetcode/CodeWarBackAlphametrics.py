import re
from collections import defaultdict

def makeVectors(puzzle):
	lettercnt = defaultdict(int)
	words = re.findall(r'[A-Z]+', puzzle)
	for word in words[:-1]:
		for i, letter in enumerate(word[::-1]):
			lettercnt[letter] += 10 ** i
	for i, letter in enumerate(words[-1][::-1]):
		lettercnt[letter] -= 10 ** i
	return list(lettercnt.keys()), list(lettercnt.values()), [list(lettercnt.keys()).index(word[0]) for word in words]

def Recussion(theta, blacklist):
	lenth = len(theta)
	Xs = {tuple(range(10))}
	minproduct, minX = 2 ** 31, []
	his = set()
	while minproduct != 0:
		temp = set()
		for X in Xs:
			for i in range(9):
				for j in range(i + 1, 10):
					newX = list(X[:])
					newX[i], newX[j] = X[j], X[i]
					newX = tuple(newX)
					if newX not in his:
						his.add(newX)
					else:
						continue
					if sum(newX[bls] == 0 for bls in blacklist) != 0:
						continue
					newpro = abs(sum(newx * y for newx, y in zip(newX[:lenth], theta)))
					(minproduct, minX) = (newpro, newX) if newpro < minproduct else (minproduct, minX)
					temp.add((newX, newpro))
		Xs = set(y[0] for y in sorted(temp, key = lambda x: x[1])[:250])
		print(len(Xs), len(temp))
		print(minproduct, '\n')
	return minX[:lenth]

def alphametics(puzzle):
	letters, theta, blacklist = makeVectors(puzzle)
	nums = Recussion(theta, blacklist)
	for i, letter in enumerate(letters):
		puzzle = puzzle.replace(letter, str(nums[i]))
	return puzzle

puzzle = 'ELEVEN + NINE + FIVE + FIVE = THIRTY'
print(alphametics(puzzle))