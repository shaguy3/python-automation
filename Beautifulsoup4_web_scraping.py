import requests
from bs4 import BeautifulSoup

test_url = 'https://www.skidrowreloaded.com/'
source = requests.get(test_url).text

soup = BeautifulSoup(source, 'lxml')

posts = soup.find_all(attrs={"class": "post"})

for post in posts:
    if not post.h2 is None:
        print(post.h2.a.text)
        print(post.h2.a['href'])
        print()
