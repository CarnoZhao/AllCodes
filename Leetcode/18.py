nums = [1, 0, -1, 0, -2, 2]
target = 0

ret = set()
nums = sorted(nums)
if nums.count(0) == 4:
	ret.add((0, 0, 0, 0))
pos = list(filter(lambda x: x >= 0, nums))
neg = list(filter(lambda x: x < 0, nums))

for i in range(len(pos)):
	idx1 = i + len(neg)
	for j in range(len(neg)):
		idx2 = j
		idx3, idx4 = 0, len(nums) - 1
		while idx3 < idx4:
			if idx3 == idx1 or idx3 == idx2:
				idx3 += 1
				continue
			if idx4 == idx1 or idx4 == idx2:
				idx4 -= 1
				continue
			sumv = nums[idx1] + nums[idx2] + nums[idx3] + nums[idx4] - target
			if sumv == 0:
				ret.add(tuple(sorted([nums[idx1], nums[idx2], nums[idx3], nums[idx4]])))
				idx3 += 1
				idx4 -= 1
			elif sumv < 0:
				idx3 += 1
			elif sumv > 0:
				idx4 -= 1

print(ret)
