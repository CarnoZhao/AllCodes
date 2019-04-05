from collections import Counter
class Solution:
    def maxSlidingWindow(self, nums, k):
        dic = Counter(nums[:k])
        maxx = max(dic.keys())
        ret = [maxx]
        for i in range(len(nums) - k):
            if dic[nums[i]] == 1:
                dic.pop(nums[i])
                if nums[i] == maxx:
                    maxx = max(max(dic.keys()), nums[i + k])
            else:
                dic[nums[i]] -= 1
            if nums[i + k] not in dic:
                dic[nums[i + k]] = 1
                maxx = max(maxx, nums[i + k])
            else:
                print(1)
                dic[nums[i + k]] += 1
            ret.append(maxx)
        return ret

sol = Solution()
nums = [-7,-8,7,5,7,1,6,0]
k = 4
ans = sol.maxSlidingWindow(nums, k)
print(ans)

import random
ls = [random.randint(0, 10) for _ in range(20)]
print(ls)