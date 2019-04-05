import numpy as np
N = 3
grid = np.random.randint(-1, 2, (N, N))
grid[0, 0], grid[-1, -1] = np.random.randint(0, 2, (2, 1))
print("grid = \n", grid)
grid = grid.tolist()
grid = [[1, 1, 1], [1, 1, 0], [0, 1, 1]]
N = len(grid)
dp = np.zeros((N, N)).tolist()
dp[0][0] = grid[0][0]
for n in range(1, 2 * N - 1):
	for i in range(N - 1, -1, -1):
		for p in range(N - 1, -1, -1):
			j, q = n - i, n - p
			print("\nNow, n = %d, i,j = %d,%d, p,q = %d,%d" % (n, i, j, p ,q))
			#print("Before change, dp = \n", np.array(dp))
			if j < 0 or j >= N or q < 0 or q >= N or grid[i][j] < 0 or grid[p][q] < 0:
				dp[i][p] = -1
				print("Poor change(1) at i=%d, p=%d,\n dp = \n" % (i, p), np.array(dp))
				continue
			if i > 0:
				dp[i][p] = max(dp[i][p], dp[i - 1][p])
				print("After change(2) at i=%d, p=%d,\n dp = \n" % (i, p), np.array(dp))
			if p > 0:
				dp[i][p] = max(dp[i][p], dp[i][p - 1])
				print("After change(3) at i=%d, p=%d,\n dp = \n" % (i, p), np.array(dp))
			if i > 0 and p > 0:
				dp[i][p] = max(dp[i][p], dp[i - 1][p - 1])
				print("After change(4) at i=%d, p=%d,\n dp = \n" % (i, p), np.array(dp))
			if dp[i][p] >= 0:
				dp[i][p] = dp[i][p] + grid[i][j] + grid[p][q] if i != p else\
					dp[i][p] + grid[i][j]
				print("After change(5) at i=%d, p=%d,\n dp = \n" % (i, p), np.array(dp))
	#print(np.array(dp))
print(int(max(dp[N - 1][N - 1], 0)))

'''public int cherryPickup(int[][] grid) {
    int N = grid.length, M = (N << 1) - 1;
    int[][] dp = new int[N][N];
    dp[0][0] = grid[0][0];
	    
    for (int n = 1; n < M; n++) {
	for (int i = N - 1; i >= 0; i--) {
	    for (int p = N - 1; p >= 0; p--) {
		int j = n - i, q = n - p;
                
		if (j < 0 || j >= N || q < 0 || q >= N || grid[i][j] < 0 || grid[p][q] < 0) {
                    dp[i][p] = -1;
                    continue;
                 }
		 
		 if (i > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p]);
		 if (p > 0) dp[i][p] = Math.max(dp[i][p], dp[i][p - 1]);
		 if (i > 0 && p > 0) dp[i][p] = Math.max(dp[i][p], dp[i - 1][p - 1]);
		 
		 if (dp[i][p] >= 0) dp[i][p] += grid[i][j] + (i != p ? grid[p][q] : 0)
             }
	 }
    }
    
    return Math.max(dp[N - 1][N - 1], 0);
}'''
'''grid = [[1,1,1,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,1],[1,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,0,0,0],[0,0,0,1,1,1,1]]
print(np.array(grid))
N = len(grid)
cnt = np.zeros((N + 1, N + 1)).tolist()
rout = []
for i in range(1, N + 1):
	for j in range(1, N + 1):
		if cnt[i - 1][j] > cnt[i][j]:
			cnt[i][j] = cnt[i - 1][j]
			rout.append(1)
		else:
			cnt[i][j] = cnt[i][j - 1]
			rout.append(0)
		if grid[i - 1][j - 1] != -1:
			cnt[i][j] += grid[i - 1][j - 1]
		else:
			cnt[i][j] -= N * N
if cnt[-1][-1] < 0:
	ret = 0
else:
	ret = cnt[-1][-1]
	i, j = N, N
	while i != 0 and j != 0:
		grid[i - 1][j - 1] = 0
		if rout.pop() == 0:
			j -= 1
		else:
			i -= 1
	grid = [x[::-1] for x in grid][::-1]
	print(np.array(grid))
	cnt = np.zeros((N + 1, N + 1)).tolist()
	for i in range(1, N + 1):
		for j in range(1, N + 1):
			cnt[i][j] = max(cnt[i - 1][j], cnt[i][j - 1])
			if grid[i - 1][j - 1] != -1:
				cnt[i][j] += grid[i - 1][j - 1]
			else:
				cnt[i][j] -= N * N
	ret += cnt[-1][-1]
print(int(ret))'''