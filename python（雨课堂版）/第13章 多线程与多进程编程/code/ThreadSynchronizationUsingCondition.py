import threading
import time
import random

class Producer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self,name=threadname)
        
    def run(self):
        global x

        time.sleep(random.randrange(1, 5))
        
        con.acquire()
        
        if x == 20:
            print('Producer waiting....')
            con.wait()
            print('Producer resumed')

        print('Producer:', end=' ')
        for i in range(20):                
            print(x, end=' ')
            x = x + 1
        print(x)
        con.notify_all()
            
        con.release()

class Consumer(threading.Thread):
    def __init__(self, threadname):
        threading.Thread.__init__(self, name =threadname)
        
    def run(self):
        global x

        time.sleep(random.randrange(1, 5))
                   
        con.acquire()
        
        if x == 0:
            print('Consumer waiting....')
            con.wait()
            print('Consumer resumed')

        print('Consumer:', end=' ')
        for i in range(20):                
            print (x, end=' ')
            x = x - 1
        print(x)
        con.notify_all()
            
        con.release()

con = threading.Condition()

x = 0

p = Producer('Producer')
c = Consumer('Consumer')

c.start()
p.start()

# 等待两个线程都运行结束
time.sleep(5)

print('\nAfter Producer and Consumer all done:',x)
