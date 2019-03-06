class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        nums = []
        opers = []
        temp = None
        do = False
        for c in s:
            if '0' <= c <= '9':
                temp = temp * 10 + ord(c) - ord('0') if temp != None else ord(c) - ord('0')
            else:
                temp = self.TempDo(temp, do, nums, opers)
                do = c in ('*', '/')
                opers.append(c)
        temp = self.TempDo(temp, do, nums, opers)
        nums = nums[::-1]
        opers = opers[::-1]
        while nums and opers:
            a, b = nums.pop(), nums.pop()
            oper = opers.pop()
            if oper == '+':
                nums.append(a + b)
            else:
                nums.append(a - b)
        return nums[0]
        
    def TempDo(self, temp, do, nums, opers):
        if temp != None:
            nums.append(temp)
            temp = None
        if do:
            a, b = nums.pop(), nums.pop()
            nums.append(a * b if opers.pop() == '*' else int(b / a))
        return temp

sol = Solution()
s = "1 - 6 + 1 - 7 / 8 + 10 / 2"
ans = sol.calculate(s)
print(ans)