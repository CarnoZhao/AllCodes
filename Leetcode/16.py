nums = [-1, 2, 1, -4]
target = 1

nums = sorted(nums)
mindis = 2 ** 31 - 1
for k in range(len(nums)):
	i, j = 0, len(nums) - 1
	while i < j:
		if i == k:
			i += 1
			continue
		elif j == k:
			j -= 1
			continue
		dis = nums[k] + nums[i] + nums[j] - target
		(i, j) = (i + 1, j) if dis < 0 else (i, j - 1)
		if abs(dis) < mindis:
			ret = dis + target
			mindis = abs(dis)
print(ret)