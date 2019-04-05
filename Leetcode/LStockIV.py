class Solution:
    def maxProfit(self, k: int, prices):
        if k <= 0 or len(prices) == 0:
            return 0
        if k > len(prices):
            ret = 0
            for i in range(1, len(prices)):
                ret += max(0, prices[i] - prices[i - 1])
            return ret
        l = [[0 for i in range(k + 1)] for j in range(len(prices))]
        g = [[0 for i in range(k + 1)] for j in range(len(prices))]
        for i in range(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            for j in range(1, k + 1):
                l[i][j] = max(g[i - 1][j - 1] + max(0, diff), l[i - 1][j] + diff)
                g[i][j] = max(l[i][j], g[i - 1][j])
                print()
                print(i, j)
                print('l\t\t\tg')
                for p in range(len(l)):
                    print(l[p][1:], '\t', g[p][1:])
        return g[-1][-1]

sol = Solution()
prices = [3,2,6,5,0,3]
k = 2
ans = sol.maxProfit(k, prices)
print(ans)