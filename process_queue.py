#author_by zhuxiaoliang
#2018-07-13 下午5:40
#队列实现进程之间的通信
'''


from multiprocessing import Process,Queue

import time

q = Queue(3)
for i in range(3):
    q.put(3)
print(q.full())#队列已满 输出True

for i in range(3):
    print(q.get())# 3

print(q.empty())#True
'''
#生产者消费者问题。
'''
from multiprocessing import Process,Queue
import time,random,os

def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('消费{}'.format(res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = 'pig%s'%i
        q.put(res)
        print('生产了{}'.format(res))
if __name__ =='__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,))
    c1 = Process(target=consumer,args=(q,))
    p1.start()
    c1.start()
    c1.join()
    print('主进程')'''
#程序卡在了最后消费者的q.get（）中，无法结束,主进程等待c1子进程结束，但是这里c1永远不会结束，最后的输入也不会打印。'''
'''
生产了pig0
生产了pig1
消费pig0
生产了pig2
消费pig1
消费pig2
生产了pig3
生产了pig4
消费pig3
生产了pig5
生产了pig6
生产了pig7
消费pig4
消费pig5
生产了pig8
消费pig6
生产了pig9
消费pig7
消费pig8
消费pig9


#如何给消费者发送信号呢？可以由主进程发送一个结束的信号给消费者，即：
from multiprocessing import Process,Queue
import time,random,os

def consumer(q):
    while True:
        res = q.get()
        if res is None:break
        time.sleep(random.randint(1,3))
        print('消费{}'.format(res))

def producer(q):
    for i in range(10):
        time.sleep(random.randint(1,3))
        res = 'pig%s'%i
        q.put(res)
        print('生产了{}'.format(res))
if __name__ =='__main__':
    q = Queue()
    p1 = Process(target=producer,args=(q,))
    c1 = Process(target=consumer,args=(q,))
    p1.start()
    c1.start()
    p1.join()
    q.put(None)
    c1.join()
    print('主进程')
'''
#输出：此时最后的打印主进程，但是这种方式缺陷明显就是有多少消费者就要发送多少次结束信号None
'''生产了pig0
消费pig0
生产了pig1
消费pig1
生产了pig2
消费pig2
生产了pig3
消费pig3
生产了pig4
生产了pig5
消费pig4
生产了pig6
消费pig5
消费pig6
生产了pig7
消费pig7
生产了pig8
生产了pig9
消费pig8
消费pig9
主进程

'''
#解决上述问题，提出了另一种队列机制。joinableQueue
#maxsize队列中最大项数。
#q.task_done(),由使用者发出信号表示q.get()方法返回的项目已经被处理。
#q.join（）方法由生产者用此方法就行阻塞，直到队列的数据被完全处理。
from multiprocessing import Process,JoinableQueue
import time ,random,os

def consumer(q):
    while True:
        res = q.get()
        time.sleep(random.randint(1,3))
        print('消费了{}'.format(res))
        q.task_done()

def producer(q):
    for i in range(5):
        time.sleep(random.randint(1,3))
        res = 'pig{}'.format(i)
        q.put(res)
        print('生产了{}'.format(res))
    q.join()

if __name__ =="__main__":
    q = JoinableQueue()
    p1 = Process(target=producer,args=(q,))
    c1 = Process(target=consumer,args=(q,))
    c1.daemon = True
    p1.start()
    c1.start()
    p1.join()
    print('主进程')
    '''
    生产了pig0
消费了pig0
生产了pig1
消费了pig1
生产了pig2
消费了pig2
生产了pig3
生产了pig4
消费了pig3
消费了pig4
主进程
    '''
#程序执行顺序：p1--c1--主进程等待p1结束，c1因为是守护线程，随着主进程结束而结束。
#切记此处要将c1设置为守护进程，随着主进程结束而结束。