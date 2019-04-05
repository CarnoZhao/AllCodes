import requests
url = 'https://www.amazon.cn/gp/product/B01M8L5Z3Y'
kv = {'user-agent': 'Mozilla/5.0'}
try:
	r = requests.get(url, headers = kv)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.encoding)
	print(r.status_code)
	print(r.text[1000:2000])
except:
	print("Fail")