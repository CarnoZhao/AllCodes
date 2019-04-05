from bs4 import BeautifulSoup
import requests

url = 'http://www.ucas.ac.cn/site/77'
r = requests.get(url)
r.raise_for_status()
r.encoding = r.apparent_encoding
soup = BeautifulSoup(r.text, 'html.parser')
childs = []
for child in soup.body.descendants:
    try:
        childs.append(child.attrs['fullname'])
    except:
        continue
with open('Names.txt', 'w') as fw:
	fw.write('\n'.join(childs))
fw.close()