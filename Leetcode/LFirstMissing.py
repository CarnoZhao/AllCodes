class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums == []:
            return 1
        i = 0
        while i < len(nums):
            try:
                num = nums[i]
                num2 = nums[num - 1]
                if num > 0 and num != num2:
                    nums[i], nums[num - 1] = nums[num - 1], nums[i]
                else:
                    i += 1
            except:
                i += 1
        print(nums)
        for i, num in enumerate(nums):
            if i != num - 1:
                break
        return i + 1
        
sol = Solution()
nums = [3, 4, -1, 1]
ans = sol.firstMissingPositive(nums)
print(ans)