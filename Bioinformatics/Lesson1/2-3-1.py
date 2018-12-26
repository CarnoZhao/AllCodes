text = 'GAGCCACCGCGATA'
ret = [0]
for c in text:
	if c == 'C':
		ret.append(ret[-1] - 1)
	elif c == 'G':
		ret.append(ret[-1] + 1)
	else:
		ret.append(ret[-1])
ret = list(map(lambda x: str(x), ret))
print(' '.join(ret))