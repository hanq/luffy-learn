import requests

title = input('key in a title:')
params = {'q': title}

url = 'https://game.51.com/search/action/game/'
resp = requests.get(url=url, params=params)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('resp_2_51game.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
