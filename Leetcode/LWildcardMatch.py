class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p == '*':
            return True
        i, j = 0, 0
        while i < len(s) and j < len(p):
            if s[i] == p[j] or p[j] == '?':
                i, j = i + 1, j + 1
            elif p[j] == '*' and j != len(p) - 1:
                for k in range(i, len(s)):
                    ret = self.isMatch(s[k:], p[j + 1:])
                    if ret:
                        break
                return ret
            elif p[j] == '*' and j == len(p) - 1:
                return True
            else:
                return False
        if i == len(s) and j == len(p):
            return True
        elif i < len(s):
            return False
        else:
            for k in range(j, len(p)):
                if p[k] != '*':
                    return False
            return True
        

sol = Solution()
s = "mississippi"
p = "m??*ss*?i*pi"
ans = sol.isMatch(s, p)
print(ans)