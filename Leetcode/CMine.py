def surrounding(matrix, i, j, r, c):
	i_s = [i] + ([i - 1] if i != 0 else []) + ([i + 1] if i != r - 1 else [])
	j_s = [j] + ([j - 1] if j != 0 else []) + ([j + 1] if j != c - 1 else [])
	return list(filter(lambda x: matrix[x[0]][x[1]] == '?', [(x, y) for x in i_s for y in j_s]))

def surrounding_mine(matrix, i, j, r, c):
	i_s = [i] + ([i - 1] if i != 0 else []) + ([i + 1] if i != r - 1 else [])
	j_s = [j] + ([j - 1] if j != 0 else []) + ([j + 1] if j != c - 1 else [])
	return len(list(filter(lambda x: matrix[x[0]][x[1]] == 'x', [(x, y) for x in i_s for y in j_s])))

def sub_click0(matrix, i, j, r, c, not_0list):
	for x, y in surrounding(matrix, i, j, r, c):
		matrix[x][y] = str(open(x, y))
		if matrix[x][y] != '0':
			not_0list.append((x,y))
	return not_0list

def click0(matrix, r, c):
	not_0list = []
	for i in range(r):
		for j in range(c):
			if matrix[i][j] != '0':
				continue
			not_0list = sub_click0(matrix, i, j, r, c, not_0list)
	return not_0list

def simpleFindMine(matrix, totalposlist, r, c):
	temp = []
	change = True
	while change:
		change = False
		for pos in totalposlist:
			surr = surrounding(matrix, pos[0], pos[1], r, c)
			if len(surr) == eval(matrix[pos[0]][pos[1]]) - surrounding_mine(matrix, pos[0], pos[1], r, c):
				for surrpos in surr:
					matrix[surrpos[0]][surrpos[1]] = 'x'
					change = True
	for pos in totalposlist:
		surr = surrounding(matrix, pos[0], pos[1], r, c)
		if eval(matrix[pos[0]][pos[1]]) == surrounding_mine(matrix, pos[0], pos[1], r, c):
			for surrpos in surr:
				matrix[surrpos[0]][surrpos[1]] = str(open(surrpos[0], surrpos[1]))
				temp.append((surrpos[0], surrpos[1]))
				change = True
	return matrix, change, temp

def solve_mine(map, n):
	matrix = [x.split(' ') for x in map.split('\n') if x != '']
	r, c = len(matrix), len(matrix[0])
	totalposlist = []
	change = True
	while change:
		poslist = click0(matrix, r, c)
		totalposlist.extend(poslist)
		matrix, change, poslist = simpleFindMine(matrix, totalposlist, r, c)
		totalposlist.extend(poslist)
		#print('\n'.join(' '.join(x) for x in matrix), '\n')
	'''cnt = 0
				for i in range(r):
					for j in range(c):
						if matrix[i][j] == '?':
							cnt += 1
				print(cnt)'''
	return '\n'.join(' '.join(x) for x in matrix)

def open(i, j):
	result1 = """
1 x 1 1 x 1
2 2 2 1 2 2
2 x 2 0 1 x
2 x 2 1 2 2
1 1 1 1 x 1
0 0 0 1 1 1"""
	result2 = """
1 1 0 1 1 1 0 0 1 1 1 0 0 0 0 1 1 1 0
x 1 0 1 x 1 0 0 2 x 2 0 0 0 0 1 x 2 1
1 1 0 2 3 3 1 1 3 x 2 0 0 0 0 1 2 x 1
0 1 1 2 x x 1 2 x 3 1 0 0 0 0 0 1 1 1
0 1 x 2 2 2 1 3 x 3 0 0 0 0 0 0 0 0 0
0 1 1 1 0 0 0 2 x 2 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 1 1 2 2 1 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 1 x x 1 0 0 0 0 0
0 0 1 1 1 0 1 1 1 0 1 2 2 1 0 0 0 0 0
0 0 1 x 2 1 3 x 2 0 0 0 0 0 0 1 1 1 0
0 0 1 1 2 x 3 x 3 1 1 0 0 0 0 1 x 1 0
0 0 0 0 1 2 3 2 2 x 1 0 0 0 0 1 1 1 0
0 0 0 0 0 1 x 1 1 1 1 0 0 0 0 0 1 1 1
0 0 1 1 2 2 2 1 0 0 0 0 0 0 0 0 1 x 1
0 0 1 x 2 x 2 1 1 0 0 0 0 0 0 0 1 1 1
0 0 1 1 2 1 3 x 3 1 0 0 0 0 0 0 0 1 1
0 0 0 0 0 0 2 x x 1 0 0 0 1 1 1 0 1 x
0 0 0 1 1 1 1 2 2 1 0 0 0 1 x 1 1 2 2
0 0 0 1 x 3 2 1 0 0 0 1 1 2 1 1 1 x 2
0 0 0 1 2 x x 1 0 0 0 1 x 1 0 1 2 3 x
0 0 0 0 1 2 2 1 1 1 1 1 1 1 0 1 x 3 2
0 0 0 0 1 1 1 1 2 x 1 1 1 1 0 2 3 x 2
0 0 0 0 1 x 1 1 x 2 1 1 x 1 0 1 x 3 x
"""
	result3 = """
0 0 0 0 0 0 0 0 1 x x 2 1 0 1 x 1 0 1 2 x
0 0 0 0 0 0 0 0 1 2 3 x 1 0 2 2 2 1 2 x 2
0 0 0 0 0 0 0 0 0 0 2 2 2 0 1 x 1 1 x 2 1
0 0 0 0 0 1 1 1 0 0 1 x 1 0 1 2 2 2 1 1 0
1 1 0 0 0 1 x 1 0 1 2 2 1 0 0 1 x 1 1 1 1
x 1 0 0 0 1 1 1 0 1 x 1 0 0 0 1 1 1 1 x 1
2 2 1 0 0 0 0 0 0 1 1 1 0 0 0 0 0 0 1 1 1
1 x 1 0 0 0 0 0 0 0 1 2 2 1 0 0 1 1 1 0 0
1 1 1 0 0 0 0 0 0 0 1 x x 1 0 0 1 x 1 0 0
"""
	return [x.split(' ') for x in result3.split('\n') if x != ''][i][j]

map1 = """
? ? ? ? ? ?
? ? ? ? ? ?
? ? ? 0 ? ?
? ? ? ? ? ?
? ? ? ? ? ?
0 0 0 ? ? ?
"""
map2 = """
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? 0
? ? 0 ? ? ? 0 0 ? ? ? 0 0 0 0 ? ? ? ?
? ? 0 ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? ?
0 ? ? ? ? ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 ? ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 0 0
0 ? ? ? 0 0 0 ? ? ? 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? 0 ? ? ? 0 ? ? ? ? 0 0 0 0 0
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 ? ? ? 0
0 0 ? ? ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 ? ? ? ? ? ? ? 0 0 0 0 ? ? ? 0
0 0 0 0 0 ? ? ? ? ? ? 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? 0 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ? ?
0 0 ? ? ? ? ? ? ? ? 0 0 0 0 0 0 0 ? ?
0 0 0 0 0 0 ? ? ? ? 0 0 0 ? ? ? 0 ? ?
0 0 0 ? ? ? ? ? ? ? 0 0 0 ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? ? ? ? ? ?
0 0 0 ? ? ? ? ? 0 0 0 ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
0 0 0 0 ? ? ? ? ? ? ? ? ? ? 0 ? ? ? ?
"""
map3 = """
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? 0 ? ? ?
0 0 0 0 0 0 0 0 ? ? ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 0 0 0 0 0 ? ? ? 0 ? ? ? ? ? ? ?
0 0 0 0 0 ? ? ? 0 0 ? ? ? 0 ? ? ? ? ? ? 0
? ? 0 0 0 ? ? ? 0 ? ? ? ? 0 0 ? ? ? ? ? ?
? ? 0 0 0 ? ? ? 0 ? ? ? 0 0 0 ? ? ? ? ? ?
? ? ? 0 0 0 0 0 0 ? ? ? 0 0 0 0 0 0 ? ? ?
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
? ? ? 0 0 0 0 0 0 0 ? ? ? ? 0 0 ? ? ? 0 0
"""
sov = solve_mine(map3, 6)
print(sov)