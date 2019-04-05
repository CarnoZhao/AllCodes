def half_find(nums, x):
	if nums[0] > nums[-1] // x:
		return nums[0], 0
	else:
		inf, sup = 0, len(nums) - 1
		while sup - inf > 1:
			mid = (inf + sup + 1) // 2
			if nums[mid] > nums[-1] // x:
				sup = mid
			else:
				inf = mid
		return nums[sup], sup
n = 2000
nums = [1]
for i in range(n - 1):
	div_5, ind_5 = half_find(nums, 5)
	newnum = div_5 * 5
	nums = nums[ind_5:]
	div_3, ind_3 = half_find(nums, 3)
	if div_3 * 3 < newnum:
		newnum = div_3 * 3
	div_2, ind_2 = half_find(nums, 2)
	if div_2 * 2 < newnum:
		newnum = div_2 * 2
	nums.append(newnum)
print(nums)
print(nums[-1])