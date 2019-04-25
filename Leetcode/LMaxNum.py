class Solution():
    def maxNumber(self, nums1, nums2, k):
        methods = []
        ret = []
        for K in range(k, 0, -1):
            if not methods:
                num, methods = self.findMax(nums1, nums2, K)
                ret.append(num)
            else:
                maxx = -1
                temp = []
                for method in methods:
                    num, newmethods = self.findMax(nums1[method[0] + 1:], nums2[method[1] + 1:], K)
                    for newmethod in newmethods:
                        newmethod[0] += method[0] + 1
                        newmethod[1] += method[1] + 1
                    if num > maxx:
                        maxx = num
                        temp = newmethods
                    elif num == maxx:
                        temp.extend(newmethods)
                ret.append(maxx)
                methods = temp
        return ret
        
    def findMax(self, nums1, nums2, k):
        lens = len(nums1) + len(nums2)
        maxx = -1
        ret = -1
        methods = []
        for i, num in enumerate(nums1):
            if num <= maxx:
                continue
            maxx = num
            if lens - i >= k:
                ret = num
                methods = [[i, -1]]
            else:
                break
        found = False
        for i, num in enumerate(nums2):
            if num < maxx or (num == maxx and found):
                continue
            elif lens - i >= k:
                if num == maxx:
                    methods.append([-1, i])
                    found = True
                else:
                    maxx = num
                    ret = num
                    methods = [[-1, i]]
            else:
                break
        print(ret, methods)
        return ret, methods


sol = Solution()
nums1 = [2,5,6,4,4,0]
nums2 = [7,3,8,0,6,5,7,6,2]
k = 15
ans = sol.maxNumber(nums1, nums2, k)
print(ans)