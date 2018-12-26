def boardToNum(board):
	ret = 0
	for row in board:
		for pos in row:
			ret = ret * 10 + pos
	return ret

def changePos(boardnum):
	ret = []
	changelists = [[1, 3], [0, 2, 4], [1, 5], [0, 4], [1, 3, 5], [2, 4]]
	ls = [(boardnum // (10 ** i)) % 10 for i in range(6)]
	idx = ls.index(0)
	changelist = changelists[idx]
	for pos in changelist:
		newls = ls[:]
		newls[pos], newls[idx] = newls[idx], newls[pos]
		ret.append(sum([newls[i] * 10 ** i for i in range(6)]))
	return ret

def main():
	board = [[1,2,3],[4,0,5]]
	boardnum = boardToNum(board)
	boardnumlist = [boardnum]
	possible = {}
	cnt = 0
	while 123450 not in possible and boardnumlist != []:
		temp = []
		cnt += 1
		for boardnum in boardnumlist:
			for num in changePos(boardnum):
				if num not in possible:
					possible[num] = cnt
					temp.append(num)
		boardnumlist = temp[:]
	ret = possible[123450] if 123450 in possible else -1
	print(ret)

main()