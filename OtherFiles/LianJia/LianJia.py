import requests
from bs4 import BeautifulSoup
import pandas as pd
import LianJiaFunctions
import numpy as np

url = lambda page: 'https://bj.lianjia.com/zufang/pg' + str(page) + 'l0/#contentList'

headers = {
    'User-Agent': 
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'
}

columns = ['names',
         'district',
         'location',
         'xaxis',
         'yaxis',
         'roomspace',
         'orientation',
         'numrooms',
         'height',
         'floors',
         'owner',
         'postdate',
         'attrs',
         'price']

data = []
name_list = []
fw = open('LianJiaTemp.txt', 'w')
hreftemp = open('hreftemp.txt', 'w')
for page in range(1, 101):
    result = requests.get(url(page), headers = headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    content_list = soup.find_all(class_ = 'content__list--item--main')
    print('Page %d ........' % page)
    for i in range(len(content_list)):
        print(i, end = '')
        line = []
        item = content_list[i]
    
        title = item.find(class_ = 'content__list--item--title twoline')
        names = title.get_text().strip()
        if names not in name_list:
            name_list.append(names)
            line.append(names)
        else:
            continue
        href = title.find('a').attrs['href']
    
        positions = [x.replace('/', '').strip() for x in item.find(class_ = 'content__list--item--des').get_text().split('\n')]
        for pos in positions:
            if pos == '':
                continue
            elif '-' in pos:
                line.extend(pos.split('-'))
                try:
                    posaxis = LianJiaFunctions.get_positions(href)
                    line.extend(posaxis)
                except:
                    line.extend((np.nan, np.nan))
                    hreftemp.write(href + '\n')
                    print('Error when getting information from %s' % href)
            elif '  ' in pos:
                line.extend([x for x in pos.split(' ') if x != ''])
            else:
                line.append(pos)

        owner = item.find(class_ = 'content__list--item--brand oneline').get_text().strip()
        line.append(owner)
    
        time = item.find(class_ = 'content__list--item--time oneline').get_text().strip()
        line.append(time)
    
        attrs_tags = item.find(class_ = 'content__list--item--bottom oneline')
        attrs = dict((x.attrs['class'][0].replace('content__item__tag--', ''), x.string) for x in attrs_tags.find_all('i'))
        line.append(attrs)
    
        price = item.find(class_ = 'content__list--item-price').find('em').get_text().strip()
        line.append(price)
        fw.write('\t'.join(str(x) for x in line) + '\n')
        if len(line) != len(columns):
            print(line)
        else:
            data.append(line)
    print()

fw.close()
hreftemp.close()
df = pd.DataFrame(data, columns = columns)
df.to_csv('LianJia.csv', sep = '\t', index = False)
print(len(df))
