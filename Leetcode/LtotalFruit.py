class Solution:
	def totalFruit(self, tree):
		i, j = 0, 0
		rights = {}
		maxlenth = 0
		while j < len(tree):
			if len(rights.keys()) < 2 or (len(rights.keys()) == 2 and tree[j] in rights):
				rights[tree[j]] = j
			elif len(rights.keys()) == 2 and tree[j] not in rights:
				i = min(rights.values()) + 1
				rights = dict([x for x in rights.items() if x[1] + 1 != i])
				rights[tree[j]] = j
			j += 1
			maxlenth = max(maxlenth, j - i)
		return maxlenth

tree = [3,3,3,1,2,1,1,2,3,3,4]
s = Solution()
ret = s.totalFruit(tree)
print(ret)