f = open('D:/Browser Download/dataset_3014_4 (1).txt')
text = f.readline().rstrip()
d = eval(f.readline().rstrip())
f.close()
print(text)
ls = list(text)
ret = []
for i in range(len(ls)):
	for nt in list('ACGT'):
		if nt != ls[i]:
			copy = ls[:]
			copy[i] = nt
			ret.append(''.join(copy))
print('\n'.join(ret))