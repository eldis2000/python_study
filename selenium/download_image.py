import requests
from selenium import webdriver

max_cnt = 20
keyword = 'walpaper'
url = f'https://www.pexels.com/ko-kr/search/{keyword}/'
driver_path = "/Users/tschoi/PycharmProjects/python_study/selenium/chromedriver"

browser = webdriver.Chrome(driver_path)
browser.maximize_window()
browser.get(url)

photo_items = browser.find_elements_by_class_name('photo-item__img')
img_urls = [x.get_attribute('data-big-src') for x in photo_items]

idx = 1
for img_url in img_urls:
    browser.get(img_url)

    res = requests.get(img_url)
    if res.ok:
        # 파일쓰기
        file_name = f'{keyword}_{idx}.jpeg'
        with open(file_name, 'wb') as f: # (w:쓰기, b:바이너리)
            f.write(res.content)
        print(f'({idx}) {file_name}') # (2) wallpaper_02.jpeg
        idx += 1

    if idx > max_cnt:
        break

browser.quit()

