#author_by zhuxiaoliang
#2018-07-09 下午10:53
#测试一
'''
from multiprocessing import Process,Pool
import time
import random
def vgg(name):
    print('{} is starting'.format(name))
    time.sleep(random.randint(1,3))
    print('{} is end'.format(name))

p = Pool()
for i in range(4):
    p.apply_async(vgg,args=(i,))
p.close()
p.join()#等待主进程结束
print('主进程')'''
"""
输出：
0 is starting
1 is starting
2 is starting
3 is starting
1 is end
2 is end
0 is end
3 is end
主进程
"""
#注释掉p.join()后,则主进程结束后，子进程直接结束。
'''
主进程
0 is starting
1 is starting
2 is starting

'''

#测试二
from multiprocessing import Process
import time
import random
def piao(name,i):
    print('%s is piaoing' %name)
    time.sleep(i)
    print('%s is piao end' %name)

p1=Process(target=piao,args=('1',1,))
p2=Process(target=piao,args=('2',2,))
p3=Process(target=piao,args=('3',3,))
p4=Process(target=piao,args=('4',4,))

p1.start()
p2.start()
p3.start()
p4.start()

p1.join()
p2.join()
p3.join()
p4.join()

print('主进程')
#程序并没有变成串行执行，更加明确join是让主进程等待，而不是子进程。