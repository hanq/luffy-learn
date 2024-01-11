"""re.findall(正则,文本模式)"""
import re

# part1: 通配符->. 字符集->[]
result = re.findall('.', 'a,b,c,d,e')
print(1, result)
result = re.findall('.', 'a,b,c,d,e,abc,a\tb\ne')
print(2, result)
result = re.findall('[ace]', 'a,b,c,d,e,abc,a\tb\ne')
print(3, result)
result = re.findall('a[ace]f', 'af,abf,acef,aacef,adsf,aef,acf,aaef')
print(4, result)
