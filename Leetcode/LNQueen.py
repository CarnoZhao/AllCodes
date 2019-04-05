class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        dic = {tuple():([], [])}
        for x in range(n):
            dic = self.f(dic, x, n)
        return len(list(dic.keys()))
    
    def f(self, dic, x, n):
        temps = {}
        for key in dic:
            for i in range(n):
                if i + x in dic[key][0] or i - x in dic[key][1] or i in key:
                    continue
                temp = list(key)
                temp.append(i)
                temps[tuple(temp)] = (dic[key][0] + [i + x], dic[key][1] + [i - x])
        return temps

sol = Solution()
n = 12
ans = sol.solveNQueens(n)
print(ans)