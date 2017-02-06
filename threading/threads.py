# -*- coding: UTF-8 -*-
from time import sleep,ctime
import threading

#音乐播发器
# def music(func,loop):
#     for i in range(loop):
#         print ("I was listening to %s! %s" % (func,ctime()))
#         sleep(2)
#
# #视频播放器
# def video(func,loop):
#     for i in range(loop):
#         print("I was at the %s! %s" % (func,ctime()))
#         sleep(5)
#
# #创建线程数组
# threads = []
#
# #创建线程t1，并添加到线程数组
# t1 = threading.Thread(target=music,args=('爱情买卖',2))
# threads.append(t1)
#
# #创建线程t2,并添加到线程数组
# t2 = threading.Thread(target=video,args=('阿凡达',3))
# threads.append(t2)
#
# if __name__ == '__main__':
#     #启动线程
#     for t in threads:
#         t.start()       #start()开始线程活动
#     #守护线程
#     for t in threads:
#         t.join()        #join()等待线程终止
#     print ('all end: %s' % ctime())


#=========>简化线程创建的麻烦<==========
#创建超级播放器
# def super_player(file_,time):
#     for i in range(2):
#         print ('Start playing: %s! %s' %(file_,ctime()))
#         sleep(time)
#
# #播放文件与播放时长
# lists = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}
#
# threads = []
# files = range(len(lists))
#
# #创建线程
# for file_,time in lists.items():   #返回可遍历的(键, 值) 元组数组。
#     t = threading.Thread(target=super_player,args=(file_,time))
#     threads.append(t)
#
# if __name__ == '__main__':
#     #启动线程
#     for t in files:
#         threads[t].start()
#     for t in files:
#         threads[t].join()
#
# print ('end: %s' %ctime() )


#===========>自定义线程类<===================
#创建线程类
class MyThread(threading.Thread):
    def __init__(self,func,args,name=''):
        threading.Thread.__init__(self)
        self.func = func
        self.args = args
        self.name = name

    def run(self):
        self.func(*self.args)

def super_play(file_,time):
    for i in range(2):
        print ('Start playing: %s! %s' %(file_,ctime()))
        sleep(time)

#播放文件与播放时长
lists = {'爱情买卖.mp3':3,'阿凡达.mp4':5,'我和你.mp3':4}

threads = []
files = range(len(lists))

#创建线程
for file_,time in lists.items():   #返回可遍历的(键, 值) 元组数组。
    # t = threading.Thread(target=super_player,args=(file_,time))
    t = MyThread(super_play,(file_,time),super_play.__name__)
    threads.append(t)

if __name__ == '__main__':
    #启动线程
    for t in files:
        threads[t].start()
    for t in files:
        threads[t].join()

print ('end: %s' %ctime() )





