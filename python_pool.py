#author_by zhuxiaoliang
#2018-07-14 下午10:58
#同步调用
'''
from  multiprocessing import Pool
import os,time

def work(n):
    print('%s run'%os.getpid())
    time.sleep(3)
    return n**2

if __name__ =='__main__':
    p = Pool(3)
    resl = []
    for i in range(5):
        #同步调用，一直等待任务执行结束为止。
        res = p.apply(work,args=(i,))
        resl.append(res)
    print(resl)'''
#异步调用
'''
from multiprocessing import Pool
import os,time
def work(n):
    print('%s run '%os.getpid())
    time.sleep(2)
    return n**2

if __name__ =='__main__':
    p = Pool(3)
    res_l = []
    for i in range(5):
        res = p.apply_async(work,args=(i,))
        res_l.append(res)
    p.close()
    p.join()
    for i in res_l:
        print(i.get())
    print('over')'''

#进程池异步调用

from multiprocessing import Pool,Process
import time

def func(msg):
    print('msg:',msg)
    time.sleep(2)
    return msg


if __name__ =='__main__':
    pool = Pool(processes=3)
    res_l = []
    for i in range(5):
        msg = 'hello %d'%(i)
        res = pool.apply_async(func,(msg,))
        res_l.append(res)
    pool.close()
    pool.join()
    print(res_l)#拿到的是进程执行完的对象
    for i in res_l:
        print(i.get())

