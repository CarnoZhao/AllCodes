import numpy as np
import time
n = 60
area = np.random.randint(0, 9, (n, n)).astype(int).tolist()
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
area = '\n'.join(['010', '010', '010'])
area = area.split('\n')
n = len(area)
area = [list(map(lambda x: eval(x), x)) for x in area]
ts = time.time()
count = []
M = n ** 2 * 9
for i in range(n + 2):
	count.append([])
	for j in range(n + 2):
		count[i].append(M)
count[1][1] = 0
while True:
	changemake = 0
	for i in range(1, n + 1):
		for j in range(1, n + 1):
			up = count[i - 1][j] + abs(area[i - 1][j - 1] - area[i - 2][j - 1]) if i != 1 else M
			down = count[i + 1][j] + abs(area[i - 1][j - 1] - area[i][j - 1]) if i != n else M
			left = count[i][j - 1] + abs(area[i - 1][j - 1] - area[i - 1][j - 2]) if j != 1 else M
			right = count[i][j + 1] + abs(area[i - 1][j - 1] - area[i - 1][j]) if j != n else M
			minstep = min(up, down, left, right)
			if minstep < count[i][j]:
				changemake = 1
				count[i][j] = minstep
	if changemake == 0:
		break
	changemake = 0
	for i in range(n, 0, -1):
		for j in range(n, 0, -1):
			up = count[i - 1][j] + abs(area[i - 1][j - 1] - area[i - 2][j - 1]) if i != 1 else M
			down = count[i + 1][j] + abs(area[i - 1][j - 1] - area[i][j - 1]) if i != n else M
			left = count[i][j - 1] + abs(area[i - 1][j - 1] - area[i - 1][j - 2]) if j != 1 else M
			right = count[i][j + 1] + abs(area[i - 1][j - 1] - area[i - 1][j]) if j != n else M
			minstep = min(up, down, left, right)
			if minstep < count[i][j]:
				changemake = 1
				count[i][j] = minstep

	if changemake == 0:
		break
te = time.time()
print(count[n][n])
print('time = %f' % (te - ts))