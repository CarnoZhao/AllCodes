from collections import Counter
with open('file', 'r') as f:
	dic = Counter([len(line) for i, line in enumerate(f) if i % 2 == 0])
return dic