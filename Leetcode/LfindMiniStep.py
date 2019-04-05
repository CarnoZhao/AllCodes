def clean(board):
	cnt, pre = 1, None
	for pos, i in enumerate(board):
		if i == pre:
			cnt += 1
		else:
			if cnt >= 3:
				board = board[:start] + board[pos:]
				break
			cnt = 1
			start = pos
		pre = i
	return board

def allclean(board):
	nex = None
	while nex != board:
		nex = clean(board)
	return nex

class Solution:
	def findMinStep(self, board, hand):
		for ball in hand:
			for i in range(len(board)):
				newboard = board.insert(i, hand)
				board

board, hand = "RBYYBBRRB", "YRBGB" 
s = Solution()
result = s.findMinStep(board, hand)
print(result)