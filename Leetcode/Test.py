table = [[0.5 ** x, x, x + 1, x + 2] for x in range(10)]
'''
[1.0, 0, 1, 2]
[0.5, 1, 2, 3]
[0.25, 2, 3, 4]
[0.125, 3, 4, 5]
[0.0625, 4, 5, 6]
'''
titles = ['energy', 'n1', 'n2', 'n3']
lenths = [max(len(str(table[i][j])) for i in range(len(table))) for j in range(len(table[0]))]
print('\n'.join('\t'.join(str(line[j]) + ' ' * (lenths[j] - len(str(line[j]))) for j in range(len(line))) for line in [titles] + table))

print()
lenths = []
for j in range(len(table[0])):
	max_lenth = max(len(str(table[i][j])) for i in range(len(table)))
	lenths.append(max_lenth)

for line in table:
	for j in range(len(line)):
		print(str(line[j]) + ' ' * (lenths[j] - len(str(line[j]))), end = '\t')
	print()