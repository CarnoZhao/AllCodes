def func1(x, M):
	ret = True
	for i in (x[0], 0):
		for j in (x[1], 0):
			if x[2] in M[i][j] or M[i][j] == [0]:
				ret = False
				break
		if ret == False:
			break
	return ret

def remove_repeat_1(x, M):
	ret = True
	for ls1 in M:
		for ls2 in ls1:
			ls = list(ls2)
			ls.append(x[2])
			if 0 in ls and ls != []: #0 exists
				ret = False
				break
			elif len(set(ls)) == 3:
				ret = False
				break
		if ret == False:
			break
	return ret

def remove_repeat_2(x, M):
	ret = True
	ls1 = M[x[0]]
	cnt = 0
	for i in range(1, len(ls1)):
		ls2 = ls1[i]
		if x[2] in ls2:
			cnt += 1
		if (x[1] != 0 and cnt >= 2) or (x[1] == 0 and cnt >= 1):
			ret = False
			break
	return ret

def remove_repeat_3(x, M):
	ret = True
	for ls1 in M:
		if x[2] in ls1[x[1]]:
			ret = False
			break
	return ret

def repeat_check(x, M):
	ret = False
	if func1(x, M):
		if remove_repeat_1(x, M):
			if remove_repeat_2(x, M):
				if remove_repeat_3(x, M):
					ret = True
	return ret

def copy_m(m):
	mx = [ \
		[[], [], [], []], \
		[[], [], [], []], \
		[[], [], [], []] \
		]
	for i in range(len(m)):
		for j in range(len(m[i])):
			for k in range(len(m[i][j])):
				mx[i][j].append(m[i][j][k])
	return mx

def count(M0, M1):
	M2 = []
	cnt = 0
	for x in M0:
		for m in M1:
			mx = copy_m(m)
			if repeat_check(x, mx):
				mx[x[0]][x[1]].append(x[2])
				M2.append(mx)
				cnt += 1
	return cnt, M2

#M = [ \
#		[[], [], [1], [1]], \
#		[[], [], [1, 2], []], \
#		[[], [], [], []] \
#	]
#x = [0, 1, 1]

lenth = 3
num_of_attr = [3, 4, 4]
M0 = []
M = []

for i in range(num_of_attr[0]):
	for j in range(num_of_attr[1]):
		for k in range(num_of_attr[2]):
			x = [i, j, k]
			M0.append(x)
			mi = [ \
				[[], [], [], []], \
				[[], [], [], []], \
				[[], [], [], []] \
				]
			mi[i][j].append(k)
			M.append(mi)
print(len(M))

for i in range(49):
	cnt, M2 = count(M0, M)
	print(cnt)
	M = list(M2)