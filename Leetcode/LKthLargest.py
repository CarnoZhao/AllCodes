class Solution:
    def findKthLargest(self, nums, k):
        if len(nums) == 1:
            return nums[0]
        large = [x for x in nums if x > nums[0]]
        if len(large) > k - 1:
            return self.findKthLargest(large, k)
        elif len(large) == k - 1:
            return nums[0]
        else:
            return self.findKthLargest([x for x in nums if x < nums[0]], k - len(large) - 1)

sol = Solution()
nums = [2,3,1,5,21,2,412,31,4,123]
k = 2
ans = sol.findKthLargest(nums, k)
print(ans)