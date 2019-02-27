class Solution:
    def findOrder(self, ns, ps):
        dicpre = dict((i, []) for i in range(ns))
        dicpost = dict((i, []) for i in range(ns))
        for post, pre in ps:
           dicpre[post].append(pre)
           dicpost[pre].append(post)
        ret = []
        change = True
        while change:
            change = False
            for key in list(dicpre.keys()):
                if not dicpre[key]:
                    change = True
                    ret.append(key)
                    dicpre.pop(key)
                for postkey in dicpost[key]:
                    dicpre[postkey].remove(key)
        return ret

            

sol = Solution()
ns = 3
ps = [[0,1],[0,2],[1,2]]
ans = sol.findOrder(ns, ps)
print(ans)