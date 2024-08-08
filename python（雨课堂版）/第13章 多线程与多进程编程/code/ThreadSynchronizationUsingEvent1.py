from threading import Thread, Event

class Producer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name = threadname)
        
    def run(self):
        for i in range(20):
            lst.append(i)
        myEvent.set()

class Consumer(Thread):
    def __init__(self, threadname):
        Thread.__init__(self, name = threadname)
        
    def run(self):
        myEvent.wait()
        for i in range(20):
            print(lst.pop())

lst = []

myEvent = Event()
# 设置初始状态
myEvent.clear()

Producer('Producer').start()
Consumer('Consumer').start()
