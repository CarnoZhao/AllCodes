class Solution:
    def largestRectangleArea(self, heights):
   
        heights.append(0)
        st, mx = [], 0
        for i in range(len(heights)):
            while st and heights[st[-1]] >= heights[i]:
                c = st.pop()
                mx = max(mx, heights[c]*(i-st[-1]-1 if st else i))
            st.append(i)
        return mx

sol = Solution()
heights = [2,1,5,6,2,3]
ans = sol.largestRectangleArea(heights)
print(ans)