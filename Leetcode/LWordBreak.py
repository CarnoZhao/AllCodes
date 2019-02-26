class Solution:
    def wordBreak(self, s: str, wordDict):
        dp = [[] for i in range(len(s) + 1)]
        dp[0] = [[0]]
        for i in range(1, len(s) + 1):
            for j in range(i):
                if not dp[j] or s[j:i] not in wordDict:
                    continue
                for dpj in dp[j]:
                    dp[i].append(dpj + [i])
        ret = []
        for x in dp[-1]:
            string = ' '.join([s[x[i - 1]:x[i]] for i in range(1, len(x))])
            ret.append(string)
        return ret

sol = Solution()
s = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
wordDict = ["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
ans = sol.wordBreak(s, wordDict)
print(ans)