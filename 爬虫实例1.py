import requests
url = "http://item.jd.com/2967929.html"
try:
    r = requests.get(url)
    r.raise_for_status() #如果状态不是200, 引发HTTPERROR异常
    r.encoding = r.apparent_encoding
    print(r.text[:1000])
except:
    print("产生异常")

