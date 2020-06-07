import urllib.request
from bs4 import BeautifulSoup

url = 'https://m.search.naver.com/search.naver?sm=mtp_hty.top&where=m&query=%ED%8C%8C%EC%9D%B4%EC%8D%AC'
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, 'html.parser')

title = soup.find_all(class_='sh_blog_title')


print(title)

