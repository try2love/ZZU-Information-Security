import threading
import random
import time

def worker(arg):
    # 假设每个线程需要不同的时间来完成准备工作
    time.sleep(random.randint(1, 20))
    # 假设已知任何线程的准备工作最多需要20秒
    # 每个线程调用wait()时，返回值不一样
    print(arg, 'entering wait status')
    r = b.wait(20)
    if r==0:
        print(arg)
        
def printOk():
    print('ok')

# 允许3个线程等待
# 如果线程调用wait()时没有指定超时时间，默认为20秒
b = threading.Barrier(parties=3, action=printOk, timeout=20)

# 创建并启动3个线程，线程数量必须与Barrier对象的parties一致
for i in range(3):
    t = threading.Thread(target=worker, args=(i,))
    t.start()
