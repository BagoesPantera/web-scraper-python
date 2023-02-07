import requests
from bs4 import BeautifulSoup
import csv

url = 'https://www.random-name-generator.com/united-states?s=408&gender=&n=5'
headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.78'
}

req = requests.get(url, headers=headers)
print(req, '\n')
soup = BeautifulSoup(req.text, 'html.parser')
items = soup.findAll('div', 'media-body')
dataHeader = ['name', 'address', 'phone', 'ssn', 'email', 'ip', 'username', 'password', 'CC', 'exp', 'iban', 'bic', 'job', 'image']
temp = []
datas = []
for count, item in enumerate(items):
    name = item.find('dd', 'h4 col-12').text.split('(')[0]
    img = item.find('img')['data-ezsrc']
    realDatas = item.findAll('dd', 'col-sm-8')
    for index, realData in enumerate(realDatas):
        temp.append(''.join(realData.text.strip().split('\n')))
        if index == 11:
            temp.insert(0, name)
            temp.append(img)
            datas.insert(count, temp)
            temp = []
            print('\n')

writer = csv.writer(open('result/result.csv', 'w', newline=''))
writer.writerow(dataHeader)
for data in datas: writer.writerow(data)