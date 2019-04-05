area = "\n".join([
  "090009000",
  "090909090",
  "000900090",
  "999999990",
  "000900090",
  "090909090",
  "090009000",
  "099999999",
  "000000000"
])
import numpy as np
import time
n = 60
area = np.random.randint(0, 9, (n, n)).astype(int).tolist()
'''area = area.split('\n')
n = len(area)
area = [list(map(lambda x: eval(x), x)) for x in area]'''
ts = time.time()
count = []
for i in range(n):
	count.append([])
	for j in range(n):
		count[i].append(0)
N = 2 * n - 1
changelayer = 0
while True:
	for ijsum in range(changelayer + 1, N):
		for i in range(max(0, ijsum - n + 1), min(n, ijsum + 1)):
			j = ijsum - i
			if i == 0:
				pluscnt = count[i][j - 1] + abs(area[i][j] - area[i][j - 1])
			elif j == 0:
				pluscnt = count[i - 1][j] + abs(area[i][j] - area[i - 1][j])
			else:
				pluscnt = min(count[i][j - 1] + abs(area[i][j] - area[i][j - 1]), \
					count[i - 1][j] + abs(area[i][j] - area[i - 1][j]))
			count[i][j] = pluscnt
	changelayer = N
	for ijsum in range(N - 2, 0, -1):
		for i in range(max(0, ijsum - n + 1), min(n, ijsum + 1)):
			j = ijsum - i
			if i == n - 1:
				pluscnt = count[i][j + 1] + abs(area[i][j] - area[i][j + 1])
			elif j == n - 1:
				pluscnt = count[i + 1][j] + abs(area[i][j] - area[i + 1][j])
			else:
				pluscnt = min(count[i][j + 1] + abs(area[i][j] - area[i][j + 1]), \
					count[i + 1][j] + abs(area[i][j] - area[i + 1][j]))
			if count[i][j] > pluscnt:
				count[i][j] = pluscnt
				changelayer = min(changelayer, ijsum)
	if changelayer == 2 * n - 1:
		break
te = time.time()
print('time = %.3f'% (te - ts))
print(count[n - 1][n - 1])