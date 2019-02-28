class Solution:
    def combinationSum3(self, k: int, n: int):
        if k == 1:
            return 1 if 1 <= n <= 9 else 0
        rets = [set()]
        for time in range(k):
            temp = []
            for ret in rets:
                for i in range(1, 10):
                    if i in ret or ret | {i} in temp:
                        continue
                    if time != k - 1 and sum(ret) + i < n:
                        temp.append(ret | {i})
                    elif time == k - 1 and sum(ret) + i == n:
                        temp.append(ret | {i})
            rets = temp
        return [list(x) for x in temp]
        
sol = Solution()
k, n = 2, 5
ans = sol.combinationSum3(k, n)
print(ans)