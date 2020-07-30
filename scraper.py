import requests
import argparse
from bs4 import BeautifulSoup


headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'GET',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Access-Control-Max-Age': '3600',
    'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
    }


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


def process_request(url):

    req = requests.get(url, headers=headers)
    soup = BeautifulSoup(req.content, 'html5lib')
    link_attachment = generate_link_attachment(url)

    if req.status_code >= 404:
        print(req.status_code)
        return

    for a_tag in soup.findAll('a'):
        link = a_tag['href']
        if not link:
            continue

        if link[0:4] != 'http':
            link = link_attachment + link

        print(link)


def main():

    parser = argparse.ArgumentParser(
                                    description='Extracts links contained in a url'
                                    )
    parser.add_argument(
                        '-u',
                        '--url',
                        nargs='?',
                        default='https://github.com/ankushduacodes',
                        help='Extracts all the links from url\
                            (if provided else extracts links from my github profile by default)'
                        )

    arg = parser.parse_args()

    if arg.url[0:4] != 'http':
        print('Invalid url')
        return

    process_request(arg.url)


if __name__ == "__main__":
    main()
