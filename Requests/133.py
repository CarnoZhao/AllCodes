import requests
kw = input("Keyword = ")
kw = {'wd': kw}
urldic = {'Baidu': 'http://www.baidu.com/s', \
	'360': 'http://www.so.com/s'}
a = 0
while a != 1 and a != 2:
	a = eval(input("Baidu (1) or 360 (2) ?"))
engine = 'Baidu' if a == 1 else '360'
url = urldic[engine]
try:
	r = requests.get(url, params = kw)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(len(r.text))
except:
	print("Fail")