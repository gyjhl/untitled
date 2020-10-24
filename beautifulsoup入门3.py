import requests
r = requests.get("https://python123.io/ws/demo.html")
demo = r.text
from bs4 import BeautifulSoup
soup = BeautifulSoup(demo, "html.parser")
#print(soup.prettify()) #将html格式转换为prettify的格式, 便于阅读, 是在每个标签后面增加一个换行符
#print(soup.a.prettify()) #查看a标签的prettify格式
#print(soup.head) #查看head的信息
#print(soup.head.contents) #head标签的儿子节点的内容,contets是目录的意思,返回的类型是列表[]
#print(soup.body.contents) #body标签的儿子节点的内容,contets是目录的意思,返回的类型是列表[]
#print(len(soup.body.contents)) #查看body标签的儿子节点的数量
#print(soup.body.contents[1])#可以用列表类型的下标来获取相关元素
#可以用for in来遍历所有的节点
# for contents in soup.body.contents:
#     print(contents)
# 查看title标签的父标签
# print(soup.title.parent)
# 查看HTML标签的父亲, 因为html是最高级的标签所以html的标签的父标签是他自己
# print(soup.html.parent)
# soup的父标签是空的

# 标签树的上行代码, 对soup的所有上行标签进行打印, 在遍历一个标签的上行标签时, 会遍历到soup本身, 因为soup没有父标签
#所以父标签是NONE, 就不能打印了
'''
for parent in soup.a.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print(soup.a.parents)

#平行遍历
# 找a标签的下一个平行标签, 是一个and标签
print(soup.a.next_sibling)
# 再下一个平行节点
print(soup.a.next_sibling.next_sibling)
# 之前的一个平行节点
'''
print(soup.a.previous_sibling)

# 再之前的一个平行节点没有返回任何输出, 说明, 这个节点没有
print(soup.a.previous_sibling.previous_sibling)


