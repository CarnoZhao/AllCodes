S = 'a23'
K = 6
chars = ['']
nums = []
for c in S:
	if c.isdigit():
		time = eval(c)
		nums[-1] *= time
		if len(nums) == len(chars):
			chars.append('')
	else:
		if len(nums) != len(chars):
			nums.append(1)
		chars[-1] += c
lenth = [0] * len(nums)
for i in range(len(nums)):
	lenth[i] = len(chars[i]) if i == 0 else nums[i - 1] + len(chars[i])
	nums[i] *= lenth[i]
	if nums[i] >= K:
		chars = chars[:i + 1]
		lenth = lenth[:i + 1]
		nums = nums[:i + 1]
		break
print(chars, lenth, nums, sep = '\n')
i = -1
while True:
	K %= lenth[i]
	if i == -len(lenth) or K == 0:
		ret = chars[i][K - 1]
		break
	elif K > nums[i - 1]:
		K -= nums[i - 1]
		ret = chars[i][K - 1]
		break
	else:
		i -= 1
print(ret)