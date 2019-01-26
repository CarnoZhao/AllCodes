class MyCalendarTwo:

    def __init__(self):
        self.points = {0: 0}

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        temp = dict(self.points.items())
        temp[start] = sorted(filter(lambda x: x[0] <= 0, map(lambda y: (y[0] - start, y[1]), temp.items())), key = lambda z: z[0])[-1][1] + 1
        temp[end] = sorted(filter(lambda x: x[0] <= 0, map(lambda y: (y[0] - end, y[1]), temp.items())), key = lambda z: z[0])[-1][1]
        for key in temp:
                    if start < key < end:
                        temp[key] += 1
        if 3 in [x[1] for x in temp.items()]:
            return False
        else:
            self.points = temp
            return True

s = MyCalendarTwo();
ls = [[],[10,20],[50,60],[10,40],[5,15],[5,10],[25,55]]
for x in ls[1:]:
    print(s.book(x[0], x[1]))