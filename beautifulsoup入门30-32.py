import requests
from bs4 import BeautifulSoup
import bs4

def getHTMLText(url):
    try:
        r = requests.get(url, timeout = 30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "爬取失败"

def fillUnivList(ulist, html):
    soup = BeautifulSoup(html, "html.parser") #html解析引擎
    for tr in soup.find('tbody').children:
        if isinstance(tr, bs4.element.Tag):  # 检查标签是不是属于bs4定义的Tag类型的标签
            tds = tr('td')
            ulist.append([tds[0].string, tds[1].string, tds[3]. string])

def printUnivList(ulist, num):
    tplt = "{0:^10}\t{1:{3}^10}\t{2:^10}"
    print(tplt.format("排名", "学校名称","总分",chr(12288)))
    for i in range(num):
        u = ulist[i]
        print(tplt.format(u[0],u[1],u[2],chr(12288)))

    print("Suc" + str(num))

def main():
    uinfo = []
    url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2016.html'
    html = getHTMLText(url)
    fillUnivList(uinfo, html)
    printUnivList(uinfo, 50)  # 20 univs
main()