def changeall(i, j, direc, num):
	direclist = range(4) if direc == 1 else range(3, -1, -1)
	iterlist = list(zip(direclist, [j] * 4, range(4)) if i == -1 else zip([i] * 4, direclist, range(4)))
	temp = []
	cnt = 0
	for outcomes in alloutcomes:
		for line in scoredic[num]:
			newout = deepcopy(outcomes)
			pair = True
			for i, j, x in iterlist:
				if newout[i][j] == 0:
					newout[i][j] = eval(line[x])
				elif newout[i][j] != eval(line[x]):
					pair = False
					break
			if pair:
				temp.append(newout)
				cnt += 1
	return temp

def clean(alloutcomes):
	temp = []
	for outcomes in alloutcomes:
		passed = True
		for i in range(4):
			ls = [outcomes[i][j] for j in range(4)]
			for num in range(1, 5):
				if ls.count(num) > 1:
					passed = False
					break
		for j in range(4):
			ls = [outcomes[i][j] for i in range(4)]
			for num in range(1, 5):
				if ls.count(num) > 1:
					passed = False
					break
		if passed:
			temp.append(outcomes)
	return temp

from itertools import permutations
from collections import defaultdict
from copy import deepcopy
scoredic = defaultdict(list)
for line in permutations('1234', 4):
	cnt, pre = 0, 0
	for pos in line:
		if eval(pos) > pre:
			pre = eval(pos)
			cnt += 1
	scoredic[cnt].append(line)
	scoredic[0].append(line)
clue = ( 0, 0, 1, 2,   
  0, 2, 0, 0,   
  0, 3, 0, 0, 
  0, 1, 0, 0 )
alloutcomes = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
for pos, num in enumerate(clue):
	if pos < 4:
		i, j, direc = -1, pos, 1
	elif pos < 8:
		i, j, direc = pos - 4, -1, -1
	elif pos < 12:
		i, j, direc = -1, 11 - pos, -1
	else:
		i, j, direc = 15 - pos, -1, 1
	alloutcomes = clean(changeall(i, j, direc, num))
print(alloutcomes)