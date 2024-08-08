##
# 服务器程序，接收代理服务器转发来的SQL指令，并返回结果
##

import sqlite3
import socket
import struct

def getData(sql):
    '''通过给定的SQL SELECT语句返回结果'''
    with sqlite3.connect(r'database.db') as conn:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
    return result

def doSql(sql):
    '''适用于DELETE/UPDATE/INSERT INTO语句，返回影响的记录条数'''
    with sqlite3.connect(r'database.db') as conn:
        cur = conn.cursor()
        result = cur.execute(sql)
    return result.rowcount

# 创建socket对象，默认使用IPV4+TCP
sockServer = socket.socket()
sockServer.bind(('', 3030))
sockServer.listen(1)

print('Server Started.....')
while True:
    # 接收客户端连接
    try:
        conn, addr = sockServer.accept()
    except:
        continue
    
    sql = conn.recv(1024).decode('gbk').lower()
    
    if sql.startswith(('update','delete','insert')):
        try:
            # 首先发送要发送的字节总数量
            # 然后再发送真实数据
            result = str(doSql(sql)).encode('gbk')
            conn.send(struct.pack('i', len(result)))
            conn.send(result)
        except:
            message = b'error'
            conn.send(struct.pack('i', len(message)))
            conn.send(message)
    elif sql.startswith('select'):
        try:
            result = str(getData(sql)).encode('gbk')
            conn.send(struct.pack('i', len(result)))
            conn.send(result)
        except:
            message = b'error'
            conn.send(struct.pack('i', len(message)))
            conn.send(message)
    
