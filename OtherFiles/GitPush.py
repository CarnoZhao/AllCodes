import time
import os
s = time.strftime("%y.%m.%d-%H:%M:%S", time.localtime())
os.system('d:; cd Codes')
os.system('git add -A')
os.system('git status')
os.system('git commit -m %s' % s)
os.system('git push')