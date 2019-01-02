import bs4
import requests
import webbrowser
import lxml

# TODO: Open google website

# TODO: Search the requested input

# TODO: Open the first five links of the search in the browser

search = input('What would you like to search? ')
search = search.replace(' ', '+')
# Got the input from the user

res = requests.get('https://www.google.com/search?q=' + search)
res.raise_for_status()
# Got a response object from the google search

soup = bs4.BeautifulSoup(res.text, features='lxml')
# Made a beautifulSoup object with the module

links = soup.select('.r a')

print(links)
