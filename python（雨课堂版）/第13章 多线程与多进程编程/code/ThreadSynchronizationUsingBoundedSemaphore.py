from threading import Thread, BoundedSemaphore
from time import time, sleep
from random import randrange

def worker(value):
    # 线程启动时间
    start = time()
    with sema:
        # 获取资源访问权限的时间
        end = time()
        t = randrange(5)
        # 冒号后面是该线程等待的时间
        print(value, ':', end-start, ':', t) 
        sleep(2)

# 同一时刻最多允许2个线程访问特定资源
sema = BoundedSemaphore(3)

# 创建并启动10个线程
for i in range(10):
    t= Thread(target=worker, args=(i,))
    t.start()
