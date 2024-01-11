import requests

url = 'https://www.xiachufang.com/search/'

# keyword = input('key in a word to search:')
keyword = '西红柿炒鸡蛋'
header = {
    'cookie': 'bid=znPYa1hN; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2218cf72b11a2248-000c9a338e74d8-4c657b58-1327104-18cf72b11a32187%22%2C%22%24device_id%22%3A%2218cf72b11a2248-000c9a338e74d8-4c657b58-1327104-18cf72b11a32187%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%7D; Hm_lvt_ecd4feb5c351cc02583045a5813b5142=1704953844; Hm_lpvt_ecd4feb5c351cc02583045a5813b5142=1704953992',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0'
}
params = {
    'keyword': keyword,
    'cat': 1001
}

resp = requests.get(url=url, params=params)
resp.encoding = 'utf-8'

dom_text = resp.text

with open('task_1_resp.html', 'w', encoding='utf-8') as fp:
    fp.write(dom_text)
