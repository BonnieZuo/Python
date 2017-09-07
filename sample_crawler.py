# -*- coding:utf-8 -*-
import urllib.request
import io, os, re, sys
import threading
import time

class myThread(threading.Thread):
    def __init__(self, url, threadID, name,delay):
        threading.Thread.__init__(self)
        self.url = url
        self.threadID = threadID
        self.name = name
        self.delay = delay
    def run(self):
        print("Starting:" + self.name,time.ctime(time.time()))
        myThread.get_Html(self.url, self.name, self.delay)
        print("Ending:" + self.name,time.ctime(time.time()))

    # 得到保存的文件完整路径，包括文件名
    def saveFile(path):  # 这个path是网页上的图片的路径
        targetPath = "E:\爬虫图片"
        if not os.path.isdir(targetPath):  # 判断target是否为目录路径
            os.mkdir(targetPath)
        pos = path.rindex('/')  # 返回最后的那个"/"的位置的数据
        t = os.path.join(targetPath, path[pos + 1:])  # 取path中的/位置后面的那个为起始，到字符串结束，为文件的名字
        return t  # t是最后保存到本地的路径

    def get_Html(url, threadName, delay):
        # 简单的爬下百度的首页网页信息
        print(url)
        sys.stdout = io.TextIOWrapper(sys.__stdout__.buffer, encoding="gb18030")  # 纯粹解决编码问题的语句
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        html = data.decode("utf-8")
        reg = r'((http://)[\S]*?\.(jpg|png|gif))'
        imagrelist = re.findall(reg, html)  # 这是一个列表
        # print(imagrelist)
        for element in imagrelist:
            if isinstance(element, tuple):
                print(element[0])
            try:
                urllib.request.urlretrieve(element[0], myThread.saveFile(element[0]))
            except:
                print("失败")

        print(threadName, ":", time.ctime(time.time()))
        time.sleep(delay)

url1 = "http://www.baidu.com"
url2 = "https://user.qzone.qq.com/501184197/infocenter"
thread1 = myThread(url1, 1, "Thread1",1)
#thread2 = myThread(url1, 1, "Thread2",4)

thread1.start()
#thread2.start()


