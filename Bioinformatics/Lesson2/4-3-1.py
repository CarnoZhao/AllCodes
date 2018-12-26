from LoadFile import LoadFile

spec = sorted(list(map(lambda x: eval(x), open(LoadFile()).readline().rstrip().split(' '))))

convolution = []
for i in range(len(spec)):
	for j in range(i + 1, len(spec)):
		difference = spec[j] - spec[i]
		if difference != 0:
			convolution.append(difference)
print(' '.join(map(lambda x: str(x), convolution)))
convolution = list(filter(lambda x: x >= 57 and x <= 200, convolution))
#print(' '.join(map(lambda x: str(x), convolution)))
#cnt = dict([[num, convolution.count(num)] for num in set(convolution)])
#print(cnt)