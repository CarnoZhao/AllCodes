class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k: int, t: int) -> bool:
        i, j = 0, 1
        window = {nums[0]}
        while j < len(nums):
            for w in window:
                if abs(w - nums[j]) <= t:
                    return True
            window.add(nums[j])
            j += 1
            if j >= k:
                window.remove(nums[i])
                i += 1
        return False

sol = Solution()
nums = [1,2,3,1]
k = 3
t = 0
ans = sol.containsNearbyAlmostDuplicate(nums, k, t)
print(ans)