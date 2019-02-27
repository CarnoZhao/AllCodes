class Solution:
    def calculateMinimumHP(self, d):
        try:
            r, c = len(d), len(d[0])
        except:
            return
        mtx = [[(0, 0) for i in range(c)] for j in range(r)]
        mtx[0][0] = (1 - d[0][0], 1) if d[0][0] <= 0 else (1, 1 + d[0][0])
        for i in range(r):
            for j in range(c):
                if i == 0 and j != 0:
                    hp = mtx[i][j - 1][1] + d[i][j]
                    mtx[i][j] = \
                        (mtx[i][j - 1][0] - hp + 1, 1) \
                        if hp <= 0 else \
                        (mtx[i][j - 1][0], hp)
                elif i != 0 and j == 0:
                    hp = mtx[i - 1][j][1] + d[i][j]
                    mtx[i][j] = \
                        (mtx[i - 1][j][0] - hp + 1, 1) \
                        if hp <= 0 else \
                        (mtx[i - 1][j][0], hp)
                elif i != 0 and j != 0:
                    hp1 = mtx[i][j - 1][1] + d[i][j]
                    tuple1 = \
                        (mtx[i][j - 1][0] - hp1 + 1, 1) \
                        if hp1 <= 0 else \
                        (mtx[i][j - 1][0], hp1)
                    hp2 = mtx[i - 1][j][1] + d[i][j]
                    tuple2 = \
                        (mtx[i - 1][j][0] - hp2 + 1, 1) \
                        if hp2 <= 0 else \
                        (mtx[i - 1][j][0], hp2)
                    mtx[i][j] = tuple1 if tuple1[0] < tuple2[0] else tuple2
        return mtx[-1][-1][0]

sol = Solution()
d = [[1,-3,3],[0,-2,0],[-3,-3,-3]]
ans = sol.calculateMinimumHP(d)
print(ans)