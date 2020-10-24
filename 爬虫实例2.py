import requests
url = "http://www.amazon.cn/gp/product/B01M8L5Z3Y"
try:
    kv = {'user-agent': 'Mozilla/5.0'}
    r = requests.get(url, headers=kv)
    r.raise_for_status() #如果状态不是200, 引发HTTPERROR异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("爬取失败")