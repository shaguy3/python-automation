import webbrowser
import requests

res = requests.get('https://www.automatetheboringstuff.com/files/rj.txt')

try:
    res.raise_for_status()
    play_file = open('Romeo_and_Juliet.txt', 'wb')
    for chunk in res.iter_content(100000):
        play_file.write(chunk)
except Exception as err:
    print(err)
