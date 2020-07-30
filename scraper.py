import requests
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }

url = "https://github.com/ankushduacodes"


def generate_link_attachment(url):
    link_attachment = ''
    slash_count = 0
    for char in url:
        if char == '/':
            slash_count += 1
        if slash_count > 2:
            break
        link_attachment += char
    return link_attachment


def main():
    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html5lib')
    link_attachment = make_it_link(url)

    if req.status_code == 400 or req.status_code == 500:
        return

    for a_tag in soup.findAll('a'):
        link = a_tag['href']
        if not link:
            continue

        if link[0] != 'h':
            link = link_attachment + link

        print(link)


if __name__ == "__main__":
    main()
