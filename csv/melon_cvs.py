import urllib.request
from bs4 import BeautifulSoup
import csv

hdr = {'User-Agent' : 'Mozilla/5.0'}
url = 'http://melon.com/chart/index.htm'

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')

lst50 = soup.select('.lst50,.lst100')

melonList = []
for i in lst50:
    temp = []
    temp.append(i.select_one('.rank').text)
    temp.append(i.select_one('.ellipsis.rank01').a.text)
    temp.append(i.select_one('.ellipsis.rank02').a.text)
    temp.append(i.select_one('.ellipsis.rank03').a.text)
    melonList.append(temp)

width open('melon_csv','w',encoding='utf-8', newline = '') as f:
    writer = cvs.writer(f)
    writer.writerow(['rank','artist', 'title', 'album'])
    writer.writerows(melonList)

