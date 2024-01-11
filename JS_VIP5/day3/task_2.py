import requests

url = 'https://sogou.com/web'

# keyword = input('key in a word to search:')
query = '繁花爷叔是谁扮演的'
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
params = {
    'query': query
}

resp = requests.get(url=url, headers=header, params=params)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('task_2_resp.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
