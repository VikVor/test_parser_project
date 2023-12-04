import requests
from bs4 import BeautifulSoup
from pprint import pprint
from tqdm import tqdm


url = 'https://realt.by/sale/flats/'
headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'}
response = requests.get(url, headers=headers)
with open('test.html', 'w', encoding='utf-8') as f:
    f.write(response.text)

with open('test.html', encoding='utf-8') as f:
    data = f.read()
soup = BeautifulSoup(data, 'lxml')
raw_links = soup.find_all('a', class_='z-1 absolute top-0 left-0 w-full h-full cursor-pointer', href=True)
links = []
for el in raw_links:
    link = f'https://realt.by{el["href"]}'
    links.append(link)
    # print(links)

for link in links:
    resp = requests.get(link, headers=headers)
    print(resp.url)
    s = BeautifulSoup(resp.text, 'lxml')
    title = s.find('h1', {
        "class": "order-1 mb-0.5 md:-order-2 md:mb-4 block w-full !inline-block lg:text-h1Lg text-h1 font-raleway font-bold flex items-center"}).text
    try:
        price = s.find('h2',
                   class_='!inline-block mr-1 lg:text-h2Lg text-h2 font-raleway font-bold flex items-center').text.replace(
        'р.', '').replace(' ', '')

    except Exception as e:
        price = ''

    description = s.find('div', class_=['text-basic-900', 'description_wrapper__tlUQE']).text
    pprint(description)

    image = s.find('div', class_='absolute inset-0').find_all('img')[1]['src']
    print(image)



    print(f'{title} - {price}')
    break


