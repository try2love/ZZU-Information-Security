import socket
import threading
import time

activeDegree = dict()
flag = 1


def main():
    global activeDegree
    global flag

    HOST = socket.gethostbyname(socket.gethostname())
    s = socket.socket(socket.AF_INET, socket.SOCK_RAW)
    s.bind((HOST, 0))
    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_ON)  # 接收所有包

    while flag:
        data, addr = s.recvfrom(65565)  # 接收一个数据包
        host = addr[0]
        activeDegree[host] = activeDegree.get(host, 0) + 1
        if addr[0] != '10.2.1.3':  # 过滤指定IP地址的消息
            print(data, addr)

    s.ioctl(socket.SIO_RCVALL, socket.RCVALL_OFF)  # 关闭混杂模式
    s.close()


t = threading.Thread(target=main)
t.start()
time.sleep(60)
flag = 0
t.join()
for item in activeDegree.items():
    print(item)
