import requests
from bs4 import BeautifulSoup

headers = {"cookie": "over18=1",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36 Edg/107.0.1418.35"}

url = input('請輸入批踢踢實業坊文章網址: ')

request = requests.get(url, headers=headers)
request.encoding = 'utf-8'

soup = BeautifulSoup(request.text, 'html.parser')

content_of_web = soup.find(id='main-content').text.split('\n')[1:]

content_of_target = []
for i, content in enumerate(content_of_web):
    if (content == ''):
        continue
    
    if (content == '--'):
        if ((content_of_web[i+1][0] == '※') and (content_of_web[i+2][0] == '※')):
            break
        
    content_of_target.append(content)

print("\n".join(content_of_target))