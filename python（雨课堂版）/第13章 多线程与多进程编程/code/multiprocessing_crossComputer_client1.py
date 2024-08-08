from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue')

#假设服务器的IP地址为10.2.1.3
m = QueueManager(address=('10.2.1.3', 30030), authkey=b'dongfuguo')
m.connect()
q = m.get_queue()

for i in range(3):
    q.put(i)
