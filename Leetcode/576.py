m, n, N, i, j = 36, 5, 50, 15, 3
#m, n, N, i, j = 2, 2, 2, 0, 0
import numpy as np
matrix = np.zeros((m,n))
cnt = 0
matrix[i][j] = 1
for move in range(N):
	temp = np.zeros((m, n))
	for r in range(m):
		for c in range(n):
			if r == 0:
				cnt = (cnt + matrix[r, c]) % (10 ** 9 + 7)
			else:
				temp[r, c] = (temp[r, c] + matrix[r - 1, c]) % (10 ** 9 + 7)
			if r == m - 1:
				cnt = (cnt + matrix[r, c]) % (10 ** 9 + 7)
			else:
				temp[r, c] = (temp[r, c] + matrix[r + 1, c]) % (10 ** 9 + 7)
			if c == 0:
				cnt = (cnt + matrix[r, c]) % (10 ** 9 + 7)
			else:
				temp[r, c] = (temp[r, c] + matrix[r, c - 1]) % (10 ** 9 + 7)
			if c == n - 1:
				cnt = (cnt + matrix[r, c]) % (10 ** 9 + 7)
			else:
				temp[r, c] = (temp[r, c] + matrix[r, c + 1]) % (10 ** 9 + 7)
	print("move = %d" % move)
	print("matrix = \n", matrix)
	print("temp = \n", temp)
	matrix = temp.copy()
	cnt %= 10 ** 9 + 7
	print("cnt = %d" % cnt)
print(int(cnt))