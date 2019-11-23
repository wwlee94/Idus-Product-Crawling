# -*- coding:utf-8 -*-

import requests
import bs4
from bs4 import BeautifulSoup
import io
import csv
import re

# 테스트 : csv 파일 리스트값 (썸네일_리스트_320) 가져오기
rf = io.open ('idus_item_list.csv','rb')
reader = csv.reader(rf)
index = 0
for item in reader:
    if index != 0: 
        split_str = item[3].split(',')
        for string in split_str:
            print(re.sub("[\[\]\'\s]",'',string))
        print('')
    index += 1
rf.close()


