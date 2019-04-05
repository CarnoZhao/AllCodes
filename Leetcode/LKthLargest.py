class Solution:
    def findKthLargest(self, nums, k):
        print(nums, k)
        if len(nums) == 1:
            return nums[0]
        large = [x for x in nums if x > nums[0]]
        less = [x for x in nums if x < nums[0]]
        if len(large) >= k:
            return self.findKthLargest(large, k)
        elif len(less) > len(nums) - k:
            return self.findKthLargest(less, len(less) + k - len(nums))
        else:
            return nums[0]

sol = Solution()
nums = [3,2,3,1,2,4,5,5,6]
k = 4
ans = sol.findKthLargest(nums, k)
print(ans)