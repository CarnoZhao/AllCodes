nums = []
a = input()
while a != '+':
    nums.append(eval(a)) 
    a = input()
ret = []
nums = sorted(nums)
while len(nums) >= 3 and nums[0] <= 0:
    i = 1
    j = len(nums) - 1
    while i < j:
        sum = nums[i] + nums[j] + nums[0]
        if sum == 0 and \
            [nums[i], nums[j], nums[0]] not in ret:
            ret.append([nums[i], nums[j], nums[0]])
        elif sum > 0:
            j -= 1
        else:
            i += 1
    del nums[0]
print(ret)
#See the correct answer on Leetcode