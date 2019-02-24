import time
import os
s = time.strftime("%y.%m.%d", time.localtime())
os.system('d:; cd Codes')
os.system('git add -A')
os.system('git commit -m %s' % s)
os.system('git push')