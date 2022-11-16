import requests, os
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57"}

search = input('請輸入要搜尋的icon關鍵字(需為英文): ')

url = f"https://www.flaticon.com/search?word={search}"

request = requests.get(url, headers= headers)
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')

if not os.path.isdir('images'):
    os.mkdir('images')

imgs = soup.find_all(width='64', limit=10)
if (len(imgs) > 0):
    for i, img in enumerate(imgs):
        link = img['data-src']
        # 瀏覽器載入後看到的src是真實網址，但原始碼並不是，因此要另外抓取data-src才能獲得真實網址

        img = requests.get(link)
        with open("images/icon" + str(i+1) + ".png", "wb") as file:
            file.write(img.content)
else:
    print('您輸入的關鍵字並沒有找到相關的圖片!!')