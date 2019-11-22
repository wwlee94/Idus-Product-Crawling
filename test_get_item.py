import requests
import bs4
from bs4 import BeautifulSoup
import io
import csv
import re


rf = io.open ('idus_item_list.csv','rb')
reader = csv.reader(rf)
for item in reader:
    print(item[1])

rf.close()


