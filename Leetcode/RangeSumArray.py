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
        return str(string)

class NumArray:

    def __init__(self, nums):
        self.Tree = Node(nums)
        self.lenth = len(nums)

    def update(self, i: int, val: int) -> None:
        if i < (len(nums) + 1) // 2:
            

    def sumRange(self, i: int, j: int) -> int:
        pass


node = Node([1, 2, 3, 4, 5])
print(node)