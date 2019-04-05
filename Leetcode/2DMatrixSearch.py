class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        try:
            r, c = len(matrix), len(matrix[0])
        except:
            return False
        if c == 0:
            return False
        if r == 1:
            left, right = 0, c
            while left <= right and left < c and right >= 0:
                mid = (left + right) // 2
                if matrix[0][mid] < target:
                    left = mid + 1
                elif matrix[0][mid] == target:
                    return True
                else:
                    right = mid - 1
            return False
        if c == 1:
            left, right = 0, r
            while left <= right and left < r and right >= 0:
                mid = (left + right) // 2
                if matrix[mid][0] < target:
                    left = mid + 1
                elif matrix[mid][0] == target:
                    return True
                else:
                    right = mid - 1
            return False
        lowest = 0
        for i in range(r):
            if matrix[i][0] <= target:
                lowest = i
        rightest = 0
        for j in range(c):
            if matrix[0][j] <= target:
                rightest = j
        for n in range(rightest + lowest, -1, -1):
            for i in range(lowest, -1, -1):
                j = n - i
                print(i , j)
                if not(0 <= j <= rightest):
                    continue
                if matrix[i][j] == target:
                    return True
        return False

        

sol = Solution()
matrix = [[1,4],[2,5]]
target = 2
ans = sol.searchMatrix(matrix, target)
print(ans)