#author_by zhuxiaoliang
#2018-07-10 下午7:33
'''
1、join用法
'''
'''
from multiprocessing import Process
import os,time
def work(name):
    print('%s is running' %name)
    time.sleep(2)
    print('%s is done ' %name)
#方式一
p1 = Process(target=work,args=(1,))
p2 = Process(target=work,args=(2,))
p3 = Process(target=work,args=(3,))


P = [p1,p2,p3]
for p in P :
   p.start()
   p.join()

#方式二
p1.start()
p2.start()
p3.start()
p1.join()
p2.join()
p3.join()

print('*******')
#方式三
for i in  range(3):
    p = Process(target=work,args=(i,))
    p.start()
    p.join()
#再次强调join用法：主进程等待子进程结束，至于等待是所有子进程还是某一个子进程由程序设定。
#方式三中：for循环中p.join()类似于p1，p2，... pi 全部等待。
#方式二中定了p1，p2，p3，全部jion。可以注释掉p2.join()，p3.join()那么主程序只等待p1结束后，直接打印****分隔符。
'''
#2、进程同步机制：锁
from multiprocessing import Process,Lock
import os,time
def work(lock):
    lock.acquire()
    print('%s is running ' %os.getpid())
    time.sleep(1)
    print('%s is running ' %os.getpid())
    lock.release()

if __name__=="__main__":
    lock = Lock()
    for i in range(3):
        p= Process(target=work,args=(lock,))
        p.start()
        p.join()
    print('end')

'''
84386 is running 
84386 is running 
84388 is running 
84388 is running 
84390 is running 
84390 is running 
end
'''

#加锁方式可以程序编程串行，效率低下