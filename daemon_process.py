#author_by zhuxiaoliang
#2018-07-10 下午7:19
from multiprocessing import Process
import time
import random

class Vgg(Process):
    def __init__(self,name):
        self.name = name
        super().__init__()
    def run(self):
        print('{} is starting'.format(self.name))
        time.sleep(random.randint(1,3))
        print('{} is end '.format(self.name))


p = Vgg('p')
#p.daemon = True #设置守护进程，主进程结束，子进程随即结束。
p.start()
p.join()
print('主进程')

