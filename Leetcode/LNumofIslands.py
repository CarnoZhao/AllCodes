class Solution:
    def numIslands(self, grid):
        try:
            r, c = len(grid), len(grid[0])
        except:
            return 0
        uf = [i for i in range(r * c)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '0':
                    continue
                if i != r - 1 and j != c - 1:
                    if grid[i + 1][j] == '1':
                        self.union(uf, i * c + j, i * c + j + c)
                    if grid[i][j + 1] == '1':
                        self.union(uf, i * c + j, i * c + j + 1)
                elif i != r - 1 and grid[i + 1][j] == '1':
                    self.union(uf, i * c + j, i * c + j + c)
                elif j != c - 1 and grid[i][j + 1] == '1':
                    self.union(uf, i * c + j, i * c + j + 1)
        father = set()
        for i in range(len(uf)):
            print(self.find(uf, i), end = ' ')
            x, y = divmod(i, c)
            if grid[x][y] == '0':
                continue
            father.add(self.find(uf, i))
        print('\n', uf)
        return len(father)
    
    def union(self, uf, x, y):
        while uf[x] != x:
            x = uf[x]
        while uf[y] != y:
            y = uf[y]
        uf[y] = uf[x]
        
    def find(self, uf, x):
        while uf[x] != x:
            x = uf[x]
        return uf[x]

sol = Solution()
grid = [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]]
ans = sol.numIslands(grid)
print(ans)