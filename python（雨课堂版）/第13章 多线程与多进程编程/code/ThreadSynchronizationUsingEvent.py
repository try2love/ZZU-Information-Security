import threading

class myThread(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name = threadname)
        
    def run(self):
        if myEvent.isSet():
            myEvent.clear()
            print(self.getName()+' is waiting...')
            myEvent.wait()
            print(self.getName()+' resumed...')
        else:
            print(self.getName())
            myEvent.set()

myEvent = threading.Event()
# 设置初始状态
myEvent.clear()

for i in range(10):
    myThread(str(i)).start()
