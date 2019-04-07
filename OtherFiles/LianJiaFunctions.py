from collections import defaultdict
import numpy as np
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

def room_num_clean(string):
    ret = defaultdict(int)
    (room, bed, dining, bath) = (
            ('房间', 'room'),
            ('室', 'bed'),
            ('厅', 'dining'),
            ('卫', 'bath')
            )
    for kind in (room, bed, dining, bath):
        try:
            ret[kind[1]] = eval(string[string.index(kind[0]) - 1])
        except:
            pass
    if room[1] in ret:
        if ret[room[1]] <= 1:
            ret[bed[1]] += ret[room[1]]
        elif ret[room[1]] <= 3:
            ret[bed[1]] += ret[room[1]] - 1
            ret[dining[1]] += 1
        else:
            ret[bed[1]] += ret[room[1]] - 2
            ret[dining[1]] += 2
        ret.pop(room[1])
    return ret

def attrs_clean(df):
    attrs_set = set()
    df["attrs"] = df.attrs.apply(eval)
    for line in df.attrs:
        attrs_set.update(line.keys())
    for attr in attrs_set:
        df[attr] = df.attrs.apply(
                lambda x: 1 if attr in x else 0)
    return

def get_positions(href):
    url = 'https://bj.lianjia.com' + href
    headers = {
            'User-Agent':
            'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}
    result = requests.get(url, headers = headers)
    soup = BeautifulSoup(result.text, 'html.parser')
    raw = [x for x in soup.find_all('script') if 'longitude' in x.get_text()][0]
    pos = [x for x in raw.get_text().split('\n') if 'longitude' in x or 'latitude' in x]
    pos = [eval(re.findall(r'\d*\.\d*', x)[0]) for x in pos]
    return pos
