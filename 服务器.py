from socket import *
import threading
from 数据处理 import getdata
address='0.0.0.0'     #监听哪些网络  127.0.0.1是监听本机 0.0.0.0是监听整个网络
port=12345             #监听自己的哪个端口
buffsize=1024          #接收从客户端发来的数据的缓存区大小
s = socket(AF_INET, SOCK_STREAM)
s.bind((address,port))
s.listen(2)     #最大连接数

def tcplink(sock,addr):
    try:
        while True:  
            recvdata=sock.recv(buffsize).decode('utf-8')
            if recvdata=='exit' or not recvdata:
                break
            senddata=getdata(recvdata)
            sock.send(senddata.encode())
        sock.close()
    except:
        senddata="数据错误，连接已关闭"
        sock.send(senddata.encode())
        sock.close()

while True:
    clientsock,clientaddress=s.accept()
    print('connect from:',clientaddress)
#传输数据都利用clientsock，和s无关
    t=threading.Thread(target=tcplink,args=(clientsock,clientaddress))  #t为新创建的线程
    t.start()
s.close()
