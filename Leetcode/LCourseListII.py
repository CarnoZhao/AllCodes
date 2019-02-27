class Solution:
    def findOrder(self, ns, ps):
        ans, uf = self.canFinish(ns, ps)
        if not ans:
            return []
        stack = []
        print(uf)
        
        
        
    def canFinish(self, ns: int, ps):
        if not ps or not ns:
            return True
        uf = [[] for _ in range(ns)]
        for post, pre in ps:
            prelist = [pre]
            total = set()
            while prelist:
                temp = []
                for pre in prelist:
                    total.add(pre)
                    temp.extend(uf[pre])
                prelist = temp
            if post in total:
                return False, []
            else:
                uf[post] = total
        return True, uf

sol = Solution()
ns = 4
ps = [[1,0],[2,0],[3,1],[3,2]]
ans = sol.findOrder(ns, ps)
print(ans)