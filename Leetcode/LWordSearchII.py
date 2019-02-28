import collections
class Solution:
    def findWords(self, board, words):
        dic = collections.defaultdict(list)
        try:
            r, c = len(board), len(board[0])
        except:
            return []
        for i in range(r):
            for j in range(c):
                if i != r - 1:
                    dic[board[i][j]].append(board[i + 1][j])
                    dic[board[i + 1][j]].append(board[i][j])
                if j != c - 1:
                    dic[board[i][j]].append(board[i][j + 1])
                    dic[board[i][j + 1]].append(board[i][j])
        words = {word for word in words if all(word[i + 1] in dic[word[i]] for i in range(len(word) - 1))}
        print(words)


sol = Solution()
board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
ans = sol.findWords(board, words)
print(ans)