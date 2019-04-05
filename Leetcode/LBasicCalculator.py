class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' '.'')
        nums = []
        opers = []
        for c in s:
            if '0' <= c <= '9':
                nums.append(ord(c) - ord('0'))
            elif c != ')':
                opers.append(c)
            else:
                self.f()

    def f(self, nums, opers):
        while nums and opers:
            oper = opers.pop()
            if oper == '(':
                break
            else:
                
            