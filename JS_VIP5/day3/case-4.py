import requests

url = 'http://www.cpta.com.cn/category/search'
param = {
    "keywords": '人力资源',
    "搜 索": "搜 索"
}
header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
resp = requests.get(url=url, data=param, headers=header)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('resp_4_cpta_search.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
