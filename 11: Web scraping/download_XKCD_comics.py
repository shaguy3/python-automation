import requests
import bs4
import os

os.mkdir(os.getcwd() + '/XKCD comics')
url = 'https://xkcd.com/'
while True:
    res = requests.get(url)
    res.raise_for_status()
    # Got the url

    soup = bs4.BeautifulSoup(res.text, features='lxml')
    comic_img_div = soup.select('div #comic img')
    img_url = url + comic_img_div[0].get('src')
    # Got the specific img url

    print('Downloading comic: ' + img_url) # Test line
    img = requests.get(img_url)
    img.raise_for_status()
    # Downloaded image

    img_file = open(os.getcwd() + '/XKCD comics/' + comic_img_div[0].get('alt') + '.jpg', 'wb')
    for chunk in img.iter_content(100000):
        img_file.write(chunk)
    img_file.close()
    # Saved the img in the "XKCD comics" directory

    if url == 'http://www.xkcd.com/1/':
        break  # End condition to the loop

    prev_link = soup.select('a[rel="prev"]')[0]
    url = 'http://www.xkcd.com' + prev_link.get('href')
    # Changed the url to the previous page

print('Done!!!')
