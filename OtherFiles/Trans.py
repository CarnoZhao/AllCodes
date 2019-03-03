def translation():
	from googletrans import Translator
	tr = Translator()
	f = open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary.txt', encoding = 'utf-8')
	with open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary2.txt', 'w') as fw:
		for line in f:
			line = line.rstrip()
			trans = tr.translate(line, dest = 'zh-CN').text
			fw.write(trans + '\n')
			print(trans)

def combination():
	f = open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary.txt', encoding = 'ANSI')
	with open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary2.txt', 'w', encoding = 'ANSI') as fw:
		pre = None
		for l in f:
			if pre == None:
				pre = l
				continue
			if pre.split('\t')[0].split(' ')[-1] != 'artery':
				fw.write(l)
			elif pre.split('\t')[0].replace('artery', 'vein') == l.split('\t')[0]:
				string = ' '.join(l.split('\t')[0].split(' ')[:-1]) + ' artery and vein\t' + pre.split('\t')[-1].rstrip()[:-2] + '动脉和静脉'
				fw.write(string + '\n')
				print(string)
			pre = l
	f.close()

def move():
	f = open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary2.txt', encoding = 'ANSI')
	with open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary.txt', 'w', encoding = 'ANSI') as fw:
		for l in f:
			fw.write(l)
	f.close()

combination()
move()
