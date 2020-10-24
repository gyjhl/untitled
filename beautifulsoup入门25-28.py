import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
import re
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")

'''
print(soup.find_all(['a','b']))

# 对标签名称的检索字符串
#如果输入的是True, 代表找出所有的soup内容
for tag in soup.find_all(True):
    print(tag.name)



# 引入正则表达式, re, 找出b开头的所有的标签
for tag in soup.find_all(re.compile('b')):
    print(tag.name)

#查找带有course属性值的p标签
print(soup.find_all('p','course'))

#查找ID属性作为link1的值作为元素
print(soup.find_all(id='link1'))

#用正则表达式表示含有link的字符串
print(soup.find_all(id=re.compile('link')))


# recursive是否检索所有的子孙标签, 默认是检索所有的True
print(soup.find_all('a',recursive=False))

# string:  <>...</>中字符串区域的检索字符串
print(soup.find_all(string= "Basic Python"))

print(soup.find_all(string=re.compile("Python")))
'''
# 实例提取HTML中所有的URL链接
#思路: 1)搜索所有的<a>标签, 2) 解析<a>标签格式, 提取href后的链接内容

for link in soup.find_all('a'):
    print(link.get('href'))
