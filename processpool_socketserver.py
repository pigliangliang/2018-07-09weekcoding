#author_by zhuxiaoliang
#2018-07-16 上午8:46
from socket import *
from multiprocessing import Pool
import os


server = socket(AF_INET,SOCK_STREAM)
server.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
server.bind(('127.0.0.1',8080))
server.listen(5)

def talk(con,client_addr):
    print('进程pid:'.format(os.getpid()))
    while True:
        try:
            msg = con.recv(1024)
            if not msg :break
            con.send(msg.upper())
        except Exception:
            break

if __name__ =='__main__':
    p = Pool()
    while True:
        conn,client_addr = server.accept()
        p.apply_async(talk,args=(conn,client_addr))
