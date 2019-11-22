# -*- coding:utf-8 -*-

import requests
import bs4
from bs4 import BeautifulSoup
import io
import csv
import re
wf = io.open('Idus_item_list.csv', 'wb')
writer = csv.writer(wf)
writer.writerow([0,'썸네일_520','썸네일_720','썸네일_리스트_320','제목','판매자','원가','할인가','할인율','설명'])


# rf = io.open ('Idus_item_url.csv','r', encoding='utf-8')
# reader = csv.reader(rf)
# for URL_BASE in reader:
#     req = requests.get(URL_BASE[0])
#     html = req.text
#     soup = BeautifulSoup(html, 'html.parser')

#     p = re.compile('url\((.*)\)')
#     # 이미지
#     product_image = soup.select(
#         '#content > div.inner-w.layout-split > section.prd-imgs > div > fieldset > ul'
#     )[0].children

#     image_thumbnail_list_320 = []
#     for child in product_image:
#         if type(child) is not bs4.element.NavigableString:
            
#             image_style = child
#             url = p.findall(image_style.get('style'))[0]
#             image_thumbnail_list_320.append(url.encode('utf-8'))

#     image_thumbnail_520 = image_thumbnail_list_320[0].split('_')[0] + '_520.jpg'
#     image_thumbnail_720 = image_thumbnail_list_320[0].split('_')[0] + '_720.jpg'

#     # 가격 (원가, 할인가, 할인률)
#     # 1. 원가
#     product_cost = soup.select(
#         '#content > div.inner-w.layout-split > section.ui-product-detail > div.prd-cost > span.txt-strong'
#     )[0].text.encode('utf-8')
#     # 2. 할인가
#     product_discount_cost = soup.select(
#         '#content > div.inner-w.layout-split > section.ui-product-detail > div.prd-cost > span.txt-cross'
#     )
#     if product_discount_cost:
#         product_discount_cost = product_discount_cost[0].text.encode('utf-8')
#     else: product_discount_cost = None
#     # 3. 할인률
#     product_discount_rate = soup.select(
#         '#content > div.inner-w.layout-split > section.ui-product-detail > div.prd-cost > span.txt-point'
#     )
#     if product_discount_rate:
#         product_discount_rate = product_discount_rate[0].text.encode('utf-8')
#     else: product_discount_rate = None 

#     # 상품명
#     product_title = soup.select(
#         '#content > div.inner-w.layout-split > section.ui-product-detail > h1'
#     )[0].text.encode('utf-8')
#     # 셀러
#     product_seller = soup.select(
#         '#content > div.inner-w.layout-split > section.ui-product-detail > div.circ-card > a.circ-label.fl > span'
#     )[0].text.encode('utf-8')
#     # 설명
#     product_description = soup.select(
#         '#prd-info > p'
#     )[0].text.encode('utf-8')

#     print(str(product_title) + ' 완료 !!')
#     # print(image_thumbnail_520)
#     # print(image_thumbnail_720)
#     # print(image_thumbnail_list_320)

#     # print(product_cost)
#     # print(product_discount_cost)
#     # print(product_discount_rate)
#     # print(product_title)
#     # print(product_seller)
#     # print(product_description)
    

# rf.close()
wf.close()

