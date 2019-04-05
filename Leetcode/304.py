class NumMatrix:

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        import numpy as np
        r, c = np.shape(matrix)
        matrix = np.array(matrix)
        self.summatrix = np.zeros((r + 1, c + 1))
        for i in range(r + 1):
            for j in range(c + 1):
                self.summatrix[i][j] = int(np.sum(matrix[:i,:j]))
        self.summatrix = self.summatrix.tolist()
        matrix = matrix.tolist()

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        return self.summatrix[row2 + 1][col2 + 1] - self.summatrix[row2 + 1][col1] \
        - self.summatrix[row1][col2 + 1] + self.summatrix[row1][col1]

matrix = [
  [3, 0, 1, 4, 2],
  [5, 6, 3, 2, 1],
  [1, 2, 0, 1, 5],
  [4, 1, 0, 1, 7],
  [1, 0, 3, 0, 5]
]
s = NumMatrix(matrix)
print(s.summatrix)