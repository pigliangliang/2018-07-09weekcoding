#author_by zhuxiaoliang
#2018-07-09 下午10:48

from socket import *

client=socket(AF_INET,SOCK_STREAM)
client.connect(('127.0.0.1',8080))


while True:
    msg=input('>>: ').strip()
    if not msg:continue

    client.send(msg.encode('utf-8'))
    while True:
        msg=client.recv(1024)
        print(msg.decode('utf-8'))

