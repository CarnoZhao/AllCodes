s = 'TAATGCCATGGGATGTT'
k = 3
d = 2
lenth = 2 * k + d
ret = []
for i in range(len(s) - lenth + 1):
	ret.append([s[i: i + k], s[i + k + d: i + lenth]])
ret = ''.join(sorted(['(' + '|'.join(x) + ')' for x in ret]))
print(ret)
