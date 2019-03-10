class Solution:
    def removeInvalidParentheses(self, s: str):
        if self.valid(s):
            return [s]
        strings = [s]
        ret = []
        while not ret:
            for s in strings:
                temp = [s[:i] + s[i + 1:] if i != len(s) - 1 else s[i:] for i in range(len(s)) if s[i] in '()']
                for tempstring in temp

    def valid(self, s):
        num = 0
        for c in s:
            if num < 0:
                break
            if c == '(':
                num += 1
            else:
                num -= 1
        return num == 0

sol = Solution()
s = "()())()"
ans = sol.removeInvalidParentheses(s)
print(ans)