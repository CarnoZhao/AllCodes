def P1():
	words = {}
	with open('Part1.txt', encoding = 'utf8') as f:
		newkey = True
		for l in f:
			if l == '\n':
				newkey = True
				continue
			if newkey:
				k = l.rstrip()
				newkey = False
				words[k] = []
			else:
				words[k].append(l.rstrip())
	with open('Part1.txt', 'w', encoding = 'utf8') as fw:			
		for key, value in words.items():
			fw.write('$$$'.join(value) + '\n')
	##invalid

def P2():
	words = []
	with open('Part2.txt', encoding = 'utf8') as f:
		for l in f:
			words.append(l.rstrip().split('\t')[1])
	with open('Part2.txt', 'w', encoding = 'utf8') as fw:
		fw.write('$$$'.join(words))

def P3():
	words = {}
	with open('Part3.txt', encoding = 'utf8') as f:
		newkey = True
		for l in f:
			if l == '\n':
				newkey = True
				continue
			if newkey:
				k = l.rstrip()
				newkey = False
				words[k] = []
			else:
				words[k].append(l.rstrip().split('\t')[-1])
	with open('Part3.txt', 'w', encoding = 'utf8') as fw:
		for key, value in words.items():
			fw.write('$$$'.join(value) + '\n')

def Paper(printtype):
	import numpy as np
	ret1, ret2, ret3 = [], [], []
	with open('Part1.txt', encoding = 'utf8') as f:
		chapter = []
		for l in f:
			chapter.append(l.rstrip().split('$$$'))
		r1 = np.random.permutation(len(chapter))[:10]
		for chap in r1:
			ret1.append(chapter[chap][np.random.randint(0, len(chapter[chap]))])
	with open('Part2.txt', encoding = 'utf8') as f:
		chapter = f.readline().rstrip().split('$$$')
		r2 = np.random.permutation(len(chapter))[:5]
		ret2 = [chapter[x] for x in r2]
	with open('Part3.txt', encoding = 'utf8') as f:
		chapter = []
		for l in f:
			chapter.append(l.rstrip().split('$$$'))
		r3 = np.random.permutation(len(chapter))[:4]
		for chap in r3:
			ret3.append(chapter[chap][np.random.randint(0, len(chapter[chap]))])
	if printtype == 'print':
		print('名词解释：')
		print('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret1)]) + '\n')
		print('简述：')
		print('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret2)]) + '\n')
		print('问答：')
		print('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret3)]) + '\n')
	elif printtype == 'write':
		with open('Paper.txt', 'w', encoding = 'utf8') as fw:
			fw.write('名词解释：\n')
			fw.write('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret1)]) + '\n\n')
			fw.write('简述：\n')
			fw.write('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret2)]) + '\n\n')
			fw.write('问答：\n')
			fw.write('\n'.join([str(x[0] + 1) + '.\t' + x[1] for x in enumerate(ret3)]) + '\n\n')

Paper('print')