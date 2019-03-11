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
        return '\n'.join(str(x) for x in string)

class NumArray:

    def __init__(self, nums):
        self.Tree = Node(nums)
        self.lenth = len(nums)

    def update(self, i: int, val: int) -> None:
        l, r = 0, self.lenth
        node = self.Tree
        plus = []
        while l < r:
            plus.append(node)
            mid = (l + r) // 2
            if i <= mid:
                r = mid
                node = node.left
            else:
                l = mid
                node = node.right
        diff = val - node.val
        for n in plus + [node]:
            n.val += diff

    def sumRange(self, i: int, j: int) -> int:
        

    def __str__(self):
        return self.Tree.__str__()


import random
na = NumArray([random.randint(0, 10) for x in range(10)])
print(na, '\n')
na.update(0, 2)
print(na)