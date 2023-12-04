import json

import requests
from bs4 import BeautifulSoup

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}

url = 'https://realt.by/sale/flats/?page=2'

response = requests.get(url, headers=headers).text
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response)
soup = BeautifulSoup(response, 'lxml').find('script', id='__NEXT_DATA__').text
data = json.loads(soup)
with open('test.json', 'w', encoding='utf-8') as f:
    f.write(json.dumps(data, ensure_ascii=False,indent= 4))
print(soup)