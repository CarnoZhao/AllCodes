import sys
import urllib
import time
from bs4 import BeautifulSoup
from selenium import webdriver


url = 'https://2.taobao.com'
# url2 = 'http://baike.baidu.com/starrank?fr=lemmaxianhua'

opts = webdriver.ChromeOptions()
opts.add_argument('--headless')
opts.add_argument('--no-sandbox')
opts.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome('/usr/bin/chromedriver', options = opts)
driver.get(url)

soup = BeautifulSoup(driver.page_source, 'html.parser')
print(soup.text)

driver.find_element_by_xpath("//p[contains(text(), '租房')]").click()
soup = BeautifulSoup(driver.page_source, "html.parser")
print(soup.text[:100])
