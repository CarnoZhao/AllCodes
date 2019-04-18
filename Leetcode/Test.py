from collections import Counter
with open('LDNF.py', 'r') as f:
	dic = Counter([len(line) for i, line in enumerate(f) if i % 2 == 0])
print(dic)