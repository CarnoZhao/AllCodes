from copy import deepcopy

class Node(object):
    def __init__(self, row, col):
        super(Node, self).__init__()
        self.left = None
        self.right = None
        self.down = None
        self.up = None
        self.row = row
        self.col = col

class dlxMatrix(object):
    def __init__(self, mtx):
        super(dlxMatrix, self).__init__()
        r = len(mtx)
        c = len(mtx[0])
        self.titles = [Node(-1, i - 1) for i in range(c + 1)]
        for i in range(len(self.titles)):
            self.titles[i].left = self.titles[i - 1]
            self.titles[i - 1].right = self.titles[i]
        for i in range(r):
            rownode = None
            for j in range(c):
                if mtx[i][j] == 0:
                    continue
                newnode = Node(i, j)
                for colnode in self.titles[::-1]:
                    if colnode.col == j:
                        newnode.up = colnode
                        colnode.down = newnode
                        break
                if rownode != None:
                    newnode.left = rownode
                    rownode.right = newnode
                rownode = newnode
                self.titles.append(newnode)
            while rownode.left != None:
                rownode = rownode.left
            newnode.right = rownode
            rownode.left = newnode
        for colstart in self.titles[1:c + 1]:
            colnode = colstart
            while colnode.down != None:
                colnode = colnode.down
            colnode.down = colstart
            colstart.up = colnode

    def removeRow(self, col):
        colnode = self.titles[col + 1]
        colnode.right.left = colnode.left
        colnode.left.right = colnode.right
        colnext = colnode.down
        while colnext != colnode:
            rownext = colnext.right
            while rownext != colnext:
                rownext.up.down = rownext.down
                rownext.down.up = rownext.up
                rownext = rownext.right
            colnext = colnext.down

    def addRow(self, col):
        colnode = self.titles[col + 1]
        colnext = colnode.up
        while colnext != colnode:
            rownext = colnext.left
            while rownext != colnext:
                rownext.up.down = rownext
                rownext.down.up = rownext
                rownext = rownext.left
            colnext = colnext.up
        colnode.right.left = colnode
        colnode.left.right = colnode

    def Solve(self, ans):
        ret = False
        head = self.titles[0]
        if head.left == head:
            return ans, True
        c = head.right
        self.removeRow(c.col)
        cnext = c.down
        while cnext != c:
            ans.append(cnext.row)
            rnext = cnext.right
            while rnext != cnext:
                self.removeRow(rnext.col)
                rnext = rnext.right
            ans, ret = self.Solve(ans)
            if not ret:
                ans.pop()
                rnext = cnext.left
                while rnext != cnext:
                    self.addRow(rnext.col)
                    rnext = rnext.left
                cnext = cnext.down
            else:
                break
        return ans, ret

class Solution:
    def addLine(self, mtx, i, j, n):
        line = [0 for i in range(324)]
        line[i * 9 + j] = 1
        line[80 + i * 9 + n] = 1
        line[161 + j * 9 + n] = 1
        line[242 + ((i // 3) * 3 + j // 3) * 9 + n] = 1
        mtx.append(line)
    
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        mtx = []
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    self.addLine(mtx, i, j, eval(board[i][j]))
                else:
                    for n in range(9):
                        self.addLine(mtx, i, j, n + 1)
        dlx = dlxMatrix(mtx)
        ans, ret = dlx.Solve([])
        for line in ans:
            idx = line.index(1)
            idx2 = line.index(1, idx + 1)
            i = idx // 9
            j = idx % 9
            n = idx2 - 80 - 9 * i
            board[i][j] = str(n)
        return ans

sol = Solution()
sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans, ret = sol.solveSudoku(sudoku)
'''mtx = [
    [0,0,1,0,1,1,0],
    [1,0,0,1,0,0,1],
    [0,1,1,0,0,1,0],
    [1,0,0,1,0,0,0],
    [0,1,0,0,0,0,1],
    [0,0,0,1,1,0,1]]
dlx = dlxMatrix(mtx)
ans, ret = dlx.Solve([])'''
print(ans, ret)