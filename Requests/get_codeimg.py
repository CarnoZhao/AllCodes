import requests
from bs4 import BeautifulSoup
url = 'http://sep.ucas.ac.cn/'
r = requests.get(url)
soup = BeautifulSoup(r.text, 'html.parser')
childs = []
for child in soup.body.descendants:
    try:
        if child.attrs['class'] == ['input-icon', 'span12']:
            childs.append(child)
    except:
        continue
codeimg = childs[2]
codeimg = codeimg.img
print("codeimg = ", codeimg)
