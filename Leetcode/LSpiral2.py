class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        ret = [[0 for i in range(n)] for j in range(n)]
        i, j, cnt, d = 0, 0, 1, 0
        ds = [(0, 1),(1, 0),(0, -1),(-1, 0)]
        while cnt <= n * n:
            ret[i][j] = cnt
            cnt += 1
            tempi, tempj = i + ds[d][0], j + ds[d][1]
            if tempi < 0 or tempj < 0 or tempi >= n or tempj >= n or ret[tempi][tempj] != 0:
                d = (d + 1) % 4
                i, j = i + ds[d][0], j + ds[d][1]
            else:
                i, j = tempi, tempj
        return ret

sol =  Solution()
n = 4
ans = sol.generateMatrix(n)
print(ans)