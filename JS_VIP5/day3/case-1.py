import requests

url = 'https://www.eastmoney.com'

resp = requests.get(url=url)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('resp_1_eastmoney.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
