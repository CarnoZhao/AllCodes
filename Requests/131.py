import requests
url = "https://item.jd.com/2967929.html"
try:
	r = requests.get(url)
	r.raise_for_status()
	r.encoding = r.apparent_encoding
	print(r.status_code)
	print(r.encoding)
	print(r.text[1:1000])
except:
	print("Fail")
