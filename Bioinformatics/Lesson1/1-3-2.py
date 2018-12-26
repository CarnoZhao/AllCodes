with open('Vibrio_cholerae.txt') as f:
	pattern = 'CTTGATCAT'
	ret = []
	for text in f:
		for i in range(len(text) - len(pattern) + 1):
			if text[i:i + len(pattern)] == pattern:
				ret.append(str(i))
print(' '.join(ret))