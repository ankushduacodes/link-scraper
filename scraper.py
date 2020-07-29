import requests
from bs4 import BeautifulSoup

# 
headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://github.com/ankushduacodes"

req = requests.get(url, headers=headers)

soup = BeautifulSoup(req.content, 'lxml')

if req.status_code == 200 or req.status_code == 300:
    for link in soup.findAll('a'):
        print(link.get('href'))


