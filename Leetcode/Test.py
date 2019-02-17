ls = [1, 2, 3, 4]
enu = list(enumerate(ls))
dic1 = dict(enu)
dic2 = dict(enu[::-1])
print(dic1 == dic2)