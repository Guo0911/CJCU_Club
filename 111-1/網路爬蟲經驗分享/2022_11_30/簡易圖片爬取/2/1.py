import requests, os
from bs4 import BeautifulSoup

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36 Edg/96.0.1054.57"}

url = f"https://guo0911.github.io/WebCrawler/Image/"

request = requests.get(url, headers= headers)
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')

if not os.path.isdir('images'):
    os.mkdir('images')

link = soup.find(alt='view2')['src']

img = requests.get(f'{url}/{link}')
with open("images/1-image.jpg", "wb") as file:
    file.write(img.content)