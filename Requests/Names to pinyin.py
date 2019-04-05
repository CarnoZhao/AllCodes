from xpinyin import Pinyin
pin = Pinyin()

fw = open('Pinyinnames.txt', 'w')
with open('Names.txt') as f:
	for l in f:
		nott = 0
		name = l.rstrip()
		pyname = pin.get_pinyin(name).replace('-', '')
		for c in pyname:
			if not (ord(c) >= ord('a') and ord(c) <= ord('z')):
				nott = 1
		if nott == 0:
			fw.write(pyname + '\n')
f.close()
fw.close()