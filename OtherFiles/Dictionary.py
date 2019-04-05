from googletrans import Translator
import tkinter
import os
tr = Translator()
while True:
    word = raw_input()
    print('This input:', word)
    out = tr.translate(word, dest = 'zh-cn').text
    print(out)