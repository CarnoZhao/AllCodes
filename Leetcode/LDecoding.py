class Solution:
    def numDecodings(self, s: 'str') -> 'int':
        ret = [1, 1]
        i = -1
        while i >= -len(s):
            temp = 0
            if s[i] != '0':
                temp += ret[-1] if ret[-1] != None else 0
                if i <= -2 and eval(s[i] + s[i + 1]) <= 26:
                    temp += ret[-2] if ret[-2] != None else 0
            ret += [temp] if temp != 0 else [None]
            i -= 1
        print(ret)
        return ret[-1] if ret[-1] != None else 0

sol = Solution()
s = '01'
ans = sol.numDecodings(s)
print(ans)