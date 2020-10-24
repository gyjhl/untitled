import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")
print(soup.a) #显示a标签
print(soup.a.name)  #显示a标签的名称
print(soup.a.parent.name)  #显示a标签的父标签
print(soup.a.parent.parent.name) #显示a标签父标签的父标签
tag = soup.a
print(tag.attrs) #获得标签的属性, 是字典格式的
print(tag.attrs['class']) #查看属性中class的值
print(tag.attrs['href']) #查看属性中链接的值, 是一个链接
print(type(tag.attrs)) #查看标签类型, 是字典类型的
print(type(tag)) #查看标签类型, 是<class 'bs4.element.Tag'>,在bs4中, tag定义了一个特殊的类型
print(soup.a.string) #a标签的字符串信息,Basic Python
print(soup.p) #p标签信息<p class="title"><b>The demo python introduces several python courses.</b></p>
print(soup.p.string) #p标签的字符串信息,The demo python introduces several python courses.
print(type(soup.p.string))# 是一个bs4特定的NavigableString类型,<class 'bs4.element.NavigableString'>
