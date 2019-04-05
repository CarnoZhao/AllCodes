class Solution:   
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        dic = {x:[] for x in range(27)}
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    dic[i].append(board[i][j])
                    dic[9 + j].append(board[i][j])
                    dic[18 + (i // 3) * 3 + j // 3].append(board[i][j])
        board, ret = self.Solve(board, dic)
        return board, ret

    def Solve(self, board, dic):
        find = False
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    find = True
                    break
            if find:
                break
        if not find:
            return board, True
        for n in range(1, 10):
            n = str(n)
            if n in dic[i] + dic[9 + j] + dic[18 + (i // 3) * 3 + j // 3]:
                continue
            board[i][j] = n
            dic[i].append(n)
            dic[9 + j].append(n)
            dic[18 + (i // 3) * 3 + j // 3].append(n)
            board, ret = self.Solve(board, dic)
            if ret:
                return board, ret
            else:
                board[i][j] = '.'
                dic[i].pop()
                dic[9 + j].pop()
                dic[18 + (i // 3) * 3 + j // 3].pop()
        return board, False

sol = Solution()
sudoku = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
ans, ret = sol.solveSudoku(sudoku)
print(ans)
