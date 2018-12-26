'''def recursion(array, nums, ret, start):
    if len(array) >= 2 and array not in ret:
        ret.append(array[:])
    for i in range(start, len(nums)):
        if len(array) == 0 or array[-1] <= nums[i]:
            array.append(nums[i])
        ret = recursion(array, nums, ret, i + 1)
        try:
            array.pop()
        except:
            pass
    return ret

nums = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
ret = []
stack = []
ret = recursion(stack, nums, ret, 0)
print(ret)'''
print('See at Leetcode')