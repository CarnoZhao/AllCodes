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

class Solution:
	def findMinStep(self, board, hand):
		return 1

board, hand = "RBYYBBRRB", "YRBGB" 
s = Solution()
result = s.findMinStep(board, hand)
print(result)
print(clean(clean('aabbbbasd')))