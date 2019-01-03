import bs4
import requests
import webbrowser

search = input('What would you like to search? ')
search = search.replace(' ', '+')
# Got the input from the user

res = requests.get('https://www.google.com/search?q=' + search)
res.raise_for_status()
# Got a response object from the google search

soup = bs4.BeautifulSoup(res.text, features='lxml')
# Made a beautifulSoup object with the module

links_html = soup.select('.r a')
# Selected all of the search links of the response

for link_html in links_html:
    webbrowser.open('https://www.google.com/' + link_html.get('href'))
    # Opened a tab with each of the searches.
