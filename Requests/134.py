import requests
import os
path = '/mnt/d/Onedrive - mails.ucas.edu.cn/大三上/机器学习/Requests/134.jpg'
url = 'http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg'
try:
	if not os.path.exists(path):
		r = requests.get(url)
		with open(path, 'wb') as f:
			f.write(r.content)
			f.close()
			print('Done')
	else:
		print('File Exists')
except:
	print('Fail')