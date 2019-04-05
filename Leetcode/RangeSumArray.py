class Node:
    def __init__(self, nums):
        self.val = sum(nums)
        if len(nums) > 1:
            self.left = Node(nums[:(len(nums) + 1) // 2])
            self.right = Node(nums[(len(nums) + 1) // 2:])
        else:
            self.left = None
            self.right = None

    def __str__(self):
        ls = [self]
        string = []
        while any(x != None for x in ls):
            temp = []
            string.append([])
            string[-1].extend(str(x.val) if x else '*' for x in ls)
            for x in ls:
                if x:
                    temp.extend((x.left, x.right))
                else:
                    temp.extend((None, None))
            ls = temp
        return '\n'.join(str(x) for x in string) + '\n'

class NumArray:

    def __init__(self, nums):
        self.Tree = Node(nums)
        self.lenth = len(nums)

    def update(self, i: int, val: int) -> None:
        l, r = 0, self.lenth - 1
        node = self.Tree
        plus = []
        while node:
            plus.append(node)
            diff = val - node.val
            mid = (l + r + 1) // 2
            if i <= mid:
                r = mid
                node = node.left
            else:
                l = mid
                node = node.right
        for n in plus:
            n.val += diff

    def sumRange(self, i: int, j: int) -> int:
        sumvalue = self.Tree.val
        if 

    def __str__(self):
        return self.Tree.__str__()


import random
p = 10
na = NumArray([x for x in range(p)])
print(na, '\n')
for i in range(p):
    na.update(i, 2)
print(na)