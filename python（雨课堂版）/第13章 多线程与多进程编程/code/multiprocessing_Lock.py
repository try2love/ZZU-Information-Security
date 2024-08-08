from multiprocessing import Process, Lock

def f(l, i):
    l.acquire()                            #获取锁
    try:
        print('hello world', i)
    finally:
        l.release()                        #释放锁

if __name__ == '__main__':
    lock = Lock()                          #创建锁对象
    for num in range(10):
        Process(target=f, args=(lock, num)).start()
