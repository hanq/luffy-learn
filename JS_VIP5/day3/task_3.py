import requests

url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'

# keyword = input('key in a word to search:')
keyword = '青岛'
header = {
    'Referer': 'http://www.kfc.com.cn/kfccda/storelist/index.aspx',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
param = {
    'op': 'keyword'
}
data = {
    'cname': '',
    'pid': '',
    'keyword': keyword,
    'pageIndex': 1,
    'pageSize': 10
}

resp = requests.post(url=url, headers=header, params=param, data=data)
resp.encoding = 'utf-8'

dom_text = resp.text
print("response:", dom_text)

with open('task_3_resp.json', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
