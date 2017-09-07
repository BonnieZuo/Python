# -*- coding:utf-8 -*-
import urllib.request
import io,os
import sys
import re


def saveFile(path):
    targetPath = 'E:\爬虫图片'
    if not os.path.isdir(targetPath):
        os.mkdir(targetPath)

    pos = path.rindex('/')
    t = os.path.join(targetPath, path[pos+1:])
    return t
# 简单的爬下百度的首页网页信息
def getHtml(url):
    global filename
    sys.stdout = io.TextIOWrapper(sys.__stdout__.buffer, encoding="gb18030")
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    data = response.read()
    html = data.decode("utf-8")
    #return html
    reg = r'(http://[\S]*?\.(jpg|png|gif))'
    imagrelist = re.findall(reg, html)  # 这是一个列表
    for element in imagrelist:
        if isinstance(element, tuple):
            print(element[0])
        try:
            urllib.request.urlretrieve(element[0], saveFile(element[0]))
        except:
            print("失败")

url = "http://www.baidu.com"
print(getHtml(url))
