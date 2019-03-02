from googletrans import Translator
tr = Translator()
f = open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary.txt', encoding = 'utf-8')
with open('D:/Onedrive - mails.ucas.edu.cn/6th Term/ContemperaryBioLab/Vocabulary2.txt', 'w') as fw:
	for line in f:
		line = line.rstrip()
		trans = tr.translate(line, dest = 'zh-CN').text
		fw.write(trans + '\n')
		print(trans)

