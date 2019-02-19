class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import defaultdict
        cnt = 0
        ret = defaultdict(list)
        rets = []
        stack = []
        mx = 0
        for c in s:
            add = False
            if c == '(':
                stack.append(c)
            else:
                try:
                    stack.pop()
                    cnt += 1
                    ret[len(stack)].append(cnt)
                    print(len(stack), cnt)
                except:
                    stack = []
                    cnt = 0
                    add = True
                    rets.append(ret)
                    ret = defaultdict(list)
        if not add:
            rets.append(ret)
        maxs = []
        for ret in rets:
            print(ret)
            if ret == {}:
                continue
            maxvalid = [max(ret[key]) for key in sorted(ret.keys())]
            ret = []
            for i in range(len(maxvalid)):
                if i == 0:
                    ret.append(maxvalid[i])
                else:
                    ret.append(maxvalid[i] - maxvalid[i - 1])
            maxs.append(max(ret) * 2)
        return max(maxs) if maxs != [] else 0

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        ret1, ret2 = self.func(s, '('), self.func(s[::-1], ')')[::-1]
        i, j = 0, 0
        while i < len(ret1) and j < len(ret2):
            if ret1[i] < ret2[j]:
                ret2[j] = ret2[j] - ret1[i]
                ret2.insert(j, ret1[i])
            elif ret1[i] > ret2[j]:
                ret1[i] = ret1[i] - ret2[j]
                ret1.insert(i, ret2[j])
            i, j = i + 1, j + 1
        return max(ret1) * 2


    def func(self, s, parent):
        stack = []
        cnt = 0
        ret = []
        for c in s:
            add = False
            if c == parent:
                stack.append(c)
            else:
                try:
                    stack.pop()
                    cnt += 1
                except:
                    if cnt != 0:
                        ret.append(cnt)
                    add = True
                    cnt = 0
        if not add and cnt != 0:
            ret.append(cnt)
        return ret



sol = Solution()
#ss = ['()((()()()))()((((())))']
ss = ["))(())()((((((())(()))((())(((((((()))())((((())())(()())))))))))((()((()(()(()()((()()()(()()()))(()()(()(())())))()())()((((("]
for s in ss:
    print(sol.longestValidParentheses2(s))