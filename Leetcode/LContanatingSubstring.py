class Solution:
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s == '' or words == []:
            return []
        from collections import Counter
        ret = []
        cnts = Counter(''.join(words))
        print(cnts)
        wordscnt = Counter(words) 
        sumlenth = len(words) * len(words[0])
        wordlenth = len(words[0])
        dic = {}
        for i in range(len(s) - sumlenth + 1):
            if i == 0:
                dic = Counter(s[:sumlenth])
            else:
                dic[s[i - 1]] -= 1
                dic[s[i - 1 + sumlenth]] += 1
            print(dic)
            if dic != cnts:
                continue
            newwords = [s[i + j:i + j + wordlenth] for j in range(0, sumlenth, wordlenth)]
            if Counter(newwords) == wordscnt:
                ret.append(i)
        return ret

sol = Solution()
s = "barfoothefoobarman"
words = ["foo","bar"]
result = sol.findSubstring(s, words)
print(result)