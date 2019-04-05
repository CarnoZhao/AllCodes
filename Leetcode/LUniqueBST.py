class Solution:
	global dic
	dic = {}
	def numTrees(self, n: 'int') -> 'int':
		if n == 1:
			return 1
		elif n in dic:
			return dic[n]
		ret = 0
		for i in range(1, n + 1):
			ret += self.numTrees(max(1, i - 1)) * self.numTrees(max(1, n - i))
		dic[n] = ret
		return ret

sol = Solution()
n = 3
ans = sol.numTrees(n)
print(ans)