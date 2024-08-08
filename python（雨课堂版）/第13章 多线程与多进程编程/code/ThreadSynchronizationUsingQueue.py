from threading import Thread
from time import sleep
from queue import Queue
from random import randrange

class Producer(Thread):
    '''自定义生产者线程类'''
    def __init__(self, threadname):
        Thread.__init__(self,\
                        name=threadname)
        
    def run(self):
        '''线程运行代码'''
        total = randrange(20)
        for i in range(total):
            # 等待随机时间后往队列中放入一个元素
            sleep(randrange(3))
            myQueue.put(i)
            print(self.getName(),\
                  ' put ', i,\
                  ' to queue.')
        # None表示生产者线程结束
        myQueue.put(None)

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self,\
                        name=threadname)
        
    def run(self):
        while True:
            sleep(randrange(3))
            item = myQueue.get()
            if item is None:
                break
            print(self.getName(),\
                  ' get ', item,\
                  ' from queue.')

# 创建队列
myQueue = Queue()

# 创建并启动生产者和消费者线程
Producer('Producer').start()
Consumer('Consumer').start()

