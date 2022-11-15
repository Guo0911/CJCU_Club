import requests, time
from bs4 import BeautifulSoup

headers = {"cookie": "over18=1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

url = input('請輸入批踢踢實業紡看板網址: ')

request = requests.get(url, headers=headers)
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')

titles = soup.find_all(class_='title')
for i, title in enumerate(titles):
    title = title.text.replace('\n', '').replace('\t', '')
    print(f'第{i+1}篇文章: {title}')
    time.sleep(0.1)