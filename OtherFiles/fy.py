from googletrans import Translator
import sys 
if len(sys.argv) == 1:
    print('Please input at least one word')
else:
    word = ' '.join(sys.argv[1:])
    tr = Translator()
    src = tr.detect(word).lang
    if src == 'en':
        dest = 'zh-cn'
    else:
        dest = 'en'
    translation = tr.translate(word, dest = dest).text
    if len(sys.argv) == 2:
        print('%s -> %s' % (word, translation))
    else:
        print('-> %s\n-> %s' % (word, translation))
