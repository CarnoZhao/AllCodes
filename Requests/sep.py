from requests import session, Request
from bs4 import BeautifulSoup
import requests

session_req = session()
url = 'http://210.77.16.21'
loginurl = ':8080/eportal/interface/index_files/pc/login_bch.js'
postData = {'userIndex': '32633037313662353833633861633363626437353637613834636664653561385f31302e3230302e3232362e3134355f323031364b38303039393135303434', \
'keepaliveInterval': 0}
req = Request('post', url + loginurl, data = postData, headers = dict(referer = url + loginurl))
prepped = req.prepare()
resp = session_req.send(prepped)
soup = BeautifulSoup(resp.content, 'html.parser')
print(soup)

'''for child in soup.descendants:
	try:
		if child.name == 'a' and \
			child.attrs['title'] == '课程网站':
			courseurl = url + child.attrs['href'] + '/801'
			break
	except:
		continue

session_co = session()
req_co = Request('post', courseurl, headers = dict(referer = courseurl))
prepped_co = req_co.prepare()
resp_co = session_req.send(prepped_co)
soup_co = BeautifulSoup(resp_co.content, 'html.parser')
print(soup_co)'''
