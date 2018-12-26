import re
from collections import defaultdict, OrderedDict

def chooseTarget(examples):
	preset, postset = set(), set()
	for eg in examples:
		eg = eg.split('=')
		preset = preset | set(filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'z', list(eg[0])))
		postset = postset | set(filter(lambda x: 'a' <= x <= 'z' or 'A' <= x <= 'z', list(eg[1])))
	return list(filter(lambda x: x not in postset, preset))[0]

def signChoose(string):
	if string  == '-':
		num = -1
	else:
		try:
			num = eval(string)
		except:
			num = 1
	return num

def Simp(string):
	while True:
		parenthisis = re.findall(r'[+-]?\d*[(][^()]*[)]', string)
		if not parenthisis:
			break
		for oneparent in parenthisis:
			parentsplit = re.split(r'[()]', oneparent)
			coe = signChoose(parentsplit[0])
			parentsplit = re.findall(r'[+-]?\d*[a-zA-Z]', parentsplit[1])
			oneform = ''
			for single in parentsplit:
				letter = single[-1]
				num = signChoose(single[:-1])
				oneform += str(num * coe) + letter if num * coe < 0 else '+' + str(num * coe) + letter
			string = string.replace(oneparent, oneform, 1)
	diction = defaultdict(int)
	string = re.findall(r'[+-]?\d*[a-zA-Z]', string)
	for single in string:
		letter = single[-1]
		num = signChoose(single[:-1])
		diction[letter] += num
	return diction

def makeEquals(examples):
	equals = OrderedDict()
	for eg in examples:
		eg = eg.replace(' ', '').split('=')
		equals[eg[1]] = eg[0]
	return equals

def dictToString(formula):
	ret = ''
	for key in formula:
		if formula[key] == 0:
			continue
		ret += '+' + str(int(formula[key])) + key if formula[key] > 0 else str(int(formula[key])) + key
	return ret, list(formula.keys())

def simplify(examples,formula):
	target = chooseTarget(examples)
	equals = makeEquals(examples)
	formula = formula.replace(' ', '')
	letterlist = []
	while letterlist != [target]:
		for key in equals:
			formula = formula.replace(key, '(%s)' % equals[key])
			print('change %s to %s' % (key, '(%s)' % equals[key]))
			print(formula, '\n')
			formula, letterlist = dictToString(Simp(formula))
			print('simplify')
			print(formula, '\n')
	return formula if formula[0] != '+' else formula[1:]

examples = ['-15y = J', '15y - 2J = a', '9y + 3J + 10a = D', '-8y + 11J + 15a - 1D = g', '3y + 17J + 2g = m', '2y + 5J + 10a + 5D + 15g + 15m = S']
formula = '-4J + 4a - 4D - 2(1J - 3S - 1J) + 2m + 2S'
# ans = -27750n
print(simplify(examples, formula))