#author_by zhuxiaoliang
#2018-07-14 下午1:20
from multiprocessing import Process,Pipe

import time,os

def consumer(p):
    left,right = p
    left.close()#管道的不用的一段被关闭
    while True:
        try:
            rec = right.recv()
            print('收到:{}'.format(rec))
        except EOFError:
            right.close()
            break

def producer(p):
    left,right = p
    right.close()
    for i in range(5):
        left.send(i)
    left.close()
if __name__ =="__main__":
    left,right = Pipe()

    c1 = Process(target=consumer,args=((left,right),))
    #c1.daemon = True
    p1 = Process(target=producer,args=((left,right),))
    #p1.daemon = True
    c1.start()
    p1.start()

    c1.join()
    #prcint('主进程')