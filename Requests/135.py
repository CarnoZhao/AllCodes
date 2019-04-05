import requests
url = 'http://m.ip138.com/ip.asp?ip='
ip = input("IP = ")
url += ip
r = requests.get(url)
print(r.text[-500:])