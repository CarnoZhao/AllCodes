class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList):
        from collections import defaultdict
        dic = defaultdict(list)
        for i in range(len(wordList)):
            for j in range(i + 1, len(wordList)):
                if sum(x != y for x, y in zip(wordList[i], wordList[j])) == 1:
                    dic[wordList[i]].append(wordList[j])
                    dic[wordList[j]].append(wordList[i])
        iters = [[beginWord]]
        ret = []
        while iters:
            temp = []
            for path in iters:
                for nex in dic[path[-1]] and nex not in path:
                    if nex == endWord:
                        ret.append(path + [nex])
                    else:
                        temp.append(path + [nex])
            if ret:
                break
            iters = temp
        return ret

sol = Solution()
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]
ans = sol.findLadders(beginWord, endWord, wordList)
print(ans)