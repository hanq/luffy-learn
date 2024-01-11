import requests

url = 'http://www.cpta.com.cn/'
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, headers=header)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('resp_3_cpta.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
