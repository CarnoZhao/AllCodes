from collections import Counter

class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        ret = []
        dic = Counter(nums)
        nums = list(dic.keys())
        for i in range(len(nums) + 1):
            ret += self.combine(nums, i)
        for num in nums:
            temp = []
            for x in ret:
                if num not in x or dic[num] == 1:
                    continue
                for i in range(1, dic[num]):
                    temp.append(x + [num] * i)
            ret += temp
        return ret
        
    def combine(self, nums, k):
        if k == 0:
            return [[]]
        elif k == 1:
            return [[x] for x in nums]
        elif len(nums) == k:
            return [nums]
        else:
            ret = [[nums[-1]] + x for x in self.combine(nums[:-1], k - 1)]
            ret += self.combine(nums[:-1], k)
            return ret        

sol = Solution()
nums = [1 for i in range(10000)]
ans = sol.subsetsWithDup(nums)
print(ans)