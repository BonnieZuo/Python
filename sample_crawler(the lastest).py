# -*- coding:utf-8 -*-
import urllib.request
import io, os, re, sys
import threading
import time

exitflag = 0
class myThread(threading.Thread):
    def __init__(self, url, threadName ,threadID,delay):
        threading.Thread.__init__(self)
        self.url = url
        self.threadID = threadID
        self.threadName = threadName
        self.delay = delay
    def run(self):
        print("Starting:" + self.threadName,time.ctime(time.time()))
        t0 = time.time()
        myThread.get_img(self.url, self.threadName, self.threadID, self.delay)
        t7 = time.time()
        print("Ending:" + self.threadName, time.ctime(time.time()))
        print("线程1执行时间：", t7-t0)

    # 得到保存的文件完整路径，包括文件名
    def saveFile(path, ID):  # 这个path是网页上的图片的路径
        x = ID -1
        targetPath = ("E:\爬虫图片", "E:\爬虫图片1")
        if not os.path.isdir(targetPath[x]):  # 判断target是否为目录路径
            os.mkdir(targetPath[x])
        pos = path.rindex('/')  # 返回最后的那个"/"的位置的数据
        t = os.path.join(targetPath[x], path[pos + 1:])  # 取path中的/位置后面的那个为起始，到字符串结束，为文件的名字
        return t  # t是最后保存到本地的路径

    def get_Html(url):
        # 简单的爬下百度的首页网页信息
        #为什么加了这一句多线程以及打印不能逐句打印
        #sys.stdout = io.TextIOWrapper(sys.__stdout__.buffer, encoding="gb18030")  # 纯粹解决编码问题的语句
        request = urllib.request.Request(url)
        response = urllib.request.urlopen(request)
        data = response.read()
        html = data.decode("utf-8")
        return html

    def get_img(html, threadName, threadID, delay):
        html = myThread.get_Html(html)
        t1 = time.time()
        reg = r'((http://|https://)[\S]*?\.(jpg|png|gif))'
        imagrelist = re.findall(reg, html)
        i = 0
        buffer = []
        save = []
        t2 = time.time()
        print("爬取信息的时间：",t2 - t1)

        #放入列表的时长为0
        while(i< len(imagrelist)):
            if ( buffer.__contains__(imagrelist[i])):
                i += 1
                continue
            else:
                buffer.append(imagrelist[i])
                i += 1
        for element in buffer:
            if isinstance(element, tuple):
                save.append(element[0])
        t3 = time.time()

        for x in range(0, len(save)):
            #打印不花时间
            if exitflag:
                threading.Thread.exit()
            print("The", threadName, " get the picture:", save[x], ":", time.ctime(time.time()))
            t5 = time.time()
            #保存的事件在0.05-0.2之间，以图片的大小来定
            urllib.request.urlretrieve(save[x], myThread.saveFile(save[x], threadID))
            t6 = time.time()
            print("保存的时间：", t6 - t5, "\n")
        print(threadName, ":", time.ctime(time.time()))


url = "http://www.baidu.com"
url2= "https://www.zhihu.com/"
thread1 = myThread(url, "Thread1", 1, 1)
thread2 = myThread(url2, "Thread2", 2, 2)

thread1.start()
thread2.start()
print("Exiting main thread")


