class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return self.permute2(nums, [])
        
    def permute2(self, nums, ret):
        rets = []
        for i in range(len(nums)):
            newret = ret + [nums[i]]
            newnums = nums[:i] + nums[i + 1:] if i < len(nums) - 1 else nums[:i]
            if newnums != []:
                rets += self.permute2(newnums, newret)
            else:
                rets.append(newret)
        return rets

sol = Solution()
nums = [1, 2, 3, 4]
ans = sol.permute(nums)
print(ans)