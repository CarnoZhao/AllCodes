import collections
class Solution:
    def findWords(self, board, words):
        try:
            r, c = len(board), len(board[0])
        except:
            return []
        words = self.clean(board, r, c, words)
        ret = []
        for word in words:
            find = False
            for i in range(r):
                for j in range(c):
                    if board[i][j] == word[0] and self.search(word[1:], board, [(i, j)], i, j, r, c):
                        ret.append(word)
                        find = True
                        break
                if find:
                    break
        return ret

    def clean(self, board, r, c, words):
        dic = collections.defaultdict(list)
        for i in range(r):
            for j in range(c):
                if i != r - 1:
                    dic[board[i][j]].append(board[i + 1][j])
                    dic[board[i + 1][j]].append(board[i][j])
                if j != c - 1:
                    dic[board[i][j]].append(board[i][j + 1])
                    dic[board[i][j + 1]].append(board[i][j])
        return {word for word in words if all(word[i + 1] in dic[word[i]] for i in range(len(word) - 1))}
            
    def search(self, word, board, used, i, j, r, c):
        if len(word) == 0:
            return True
        dircs = []
        if i != 0:
            dircs.append((i - 1, j))
        if j != 0:
            dircs.append((i, j - 1))
        if i != r - 1:
            dircs.append((i + 1, j))
        if j != c - 1:
            dircs.append((i, j + 1))
        for x, y in dircs:
            if board[x][y] == word[0] and (x, y) not in used:
                if len(word) == 1:
                    ret = True
                else:
                    ret = self.search(word[1:], board, used + [(x, y)], x, y, r, c)
                if ret:
                    return True
        return False
                


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