class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        ret = []
        while lists != []:
            nex = ListNode(min([node.val for node in lists]))
            ret.append(nex.val)
            print(ret)
            for i, node in enumerate(lists):
                if node.val == nex.val:
                    if node.next != None:
                        lists[i] = node.next
                    else:
                        del lists[i]
                    break
                print([NodetoList(x) for x in lists])
        return ListtoNode(ret)

def NodetoList(node):
    ret = []
    while node != None:
        ret.append(node.val)
        node = node.next
    return ret

def ListtoNode(ls):
    start = None
    for i in ls:
        newnode = ListNode(i)
        if start == None:
            start = newnode
            nex = start
        else:
            nex.next = newnode
            nex = nex.next
    return start

s = Solution()
ls = [[1,4,5],[1,3,4],[2,6]]
nodes = [ListtoNode(x) for x in ls]
ans = s.mergeKLists(nodes)
print(NodetoList(ans))