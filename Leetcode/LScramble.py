class Solution:
    def isScramble(self, s1: 'str', s2: 'str') -> 'bool':
        if set(s1) != set(s2):
            return False
        elif len(s1) == 0 and len(s2) == 0:
            return True
        elif len(s1) == 1 and len(s2) == 1:
            return s1 == s2
        elif len(s1) == 2 and len(s2) == 2:
            return s1 == s2 or s1 == s2[::-1]
        else:
            ret = False
            for i in range(1, len(s1)):
                ret = ret or (self.isScramble(s1[:i], s2[-i:]) and self.isScramble(s1[i:], s2[:len(s2) - i])) or (self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]))
                if ret:
                    return ret
            return False

sol = Solution()
s1 = "ccabcbabcbabbbbcbb"
s2 = "bbbbabccccbbbabcba"
ans = sol.isScramble(s1, s2)
print(ans)