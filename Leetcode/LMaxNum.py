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

		return self.findMax(nums1, nums2, k)
		
	def findMax(self, nums1, nums2, k):
		lens = len(nums1) + len(nums2)
		maxx = -1
		for num in nums1 + nums2:
			if num >= maxx:
				maxx = num
			else:
				continue
		# for num in sorted(set(nums1 + nums2), reverse = True):
			head1 = self.index(nums1, num)
			head2 = self.index(nums2, num)
			if lens - head1 >= k and lens - head2 >= k and head1 != -1 and head2 != -1:
				ret = [num, [[head1, -1], [-1, head2]]]
			elif lens - head1 >= k and head1 != -1:
				ret = [num, [[head1, -1]]]
			elif lens - head2 >= k and head2 != -1:
				ret = [num, [[-1, head2]]]
		return ret

	def index(self, nums, n):
		for i, num in enumerate(nums):
			if num == n:
				return i
		return -1


sol = Solution()
nums1 = [6,4,7,8,6,5,5,3,1,7,4,9,9,5,9,6,1,7,1,3,6,3,0,8,2,1,8,0,0,7,3,9,3,1,3,7,5,9,4,3,5,8,1,9,5,6,5,7,8,6,6,2,0,9,7,1,2,1,7,0,6,8,5,8,1,6,1,5,8,4]
nums2 = [3,0,0,1,4,3,4,0,8,5,9,1,5,9,4,4,4,8,0,5,5,8,4,9,8,3,1,3,4,8,9,4,9,9,6,6,2,8,9,0,8,0,0,0,1,4,8,9,7,6,2,1,8,7,0,6,4,1,8,1,3,2,4,5,7,7,0,4,8,4]
k = 70
ans = sol.maxNumber(nums1, nums2, k)
print(ans)