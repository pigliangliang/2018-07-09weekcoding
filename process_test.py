#author_by zhuxiaoliang
#2018-07-09 下午10:38
'''
from multiprocessing import Process
n  = 100
def work():
    #global n
    n = 10
    print('子进程：',n)
if __name__ =="__main__":
    p = Process(target=work())
    p.start()
    print('主进程：',n)
'''

from  socket import *
from multiprocessing import Process



server =socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(conn,client_addr):
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:break
            conn.send(msg.upper())
        except Exception:
            break

if __name__ == '__main__':
    while True:
        conn,client_addr = server.accept()
        p = Process(target=talk,args=(conn,client_addr))
        p.start()
