def findMinDiff(temp, startend, S_or_E):
    minvalue = 2 ** 31 - 1
    for timepoint, overlap in temp.items():
        if timepoint > startend:
            continue
        value = startend - timepoint
        if value < minvalue:
            minvalue = value
            tempvalue = overlap + 1 if S_or_E == 'start' else max(overlap - 1, 0)
    return tempvalue

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
        temp[start] = findMinDiff(temp, start, 'start')
        for key in temp:
            if start < key <= end:
                temp[key] += 1
        temp[end] = findMinDiff(temp, end, 'end')
        #print(temp)
        if 3 in temp.values():
            return False
        else:
            self.points = temp
            return True

s = MyCalendarTwo();
ls = [[],[47,50],[1,10],[27,36],[40,47],[20,27],[15,23],[10,18],[27,36],[17,25],[8,17],[24,33],[23,28],[21,27],[47,50],[14,21],[26,32],[16,21],[2,7],[24,33],[6,13],[44,50],[33,39],[30,36],[6,15],[21,27],[49,50],[38,45],[4,12],[46,50],[13,21]]
for x in ls[1:]:
    print(s.book(x[0], x[1]), end = ' ')
    print(x)
'''for x in ls[1:]:
    for i in range(x[0]):
        print(' ', end = '')
    for i in range(x[0], x[1]):
        print('-', end = '')
    print()'''