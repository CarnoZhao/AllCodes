from collections import defaultdict

def simplify(poly):
	polylist = [x for x in ['-' + x if i != 0 else x for i, x in enumerate(poly.split('-'))]]
	pairlist = defaultdict(int)
	for pairs in polylist:
		if pairs == '':
			continue
		pairs = pairs.split('+')
		for pair in pairs:
			num, letter, sign = '', '', 1
			for char in pair:
				if char <= 'z' and char >= 'a':
					letter += char
				elif char <= '9' and char >= '0':
					num += char
				elif char == '-':
					sign = -1
			num = sign * eval(num) if num != '' else sign
			letter = ''.join(sorted(letter))
			pairlist[letter] += num
	keylist = sorted(pairlist.keys(), key = lambda x: str(len(x)) + x)
	print(pairlist)
	print(keylist)
	ret = ''
	for key in keylist:
		num = pairlist[key]
		if num == 0:
			continue
		pair = str(num) + key if num not in (1, -1) else str(num)[:-1] + key
		try:
			if pair[0] != '-':
				pair = '+' + pair if ret != '' else pair
		except:
			pass
		ret += pair
	print(ret)

poly = "-a+5ab+3a-c-2a"	
simplify(poly)