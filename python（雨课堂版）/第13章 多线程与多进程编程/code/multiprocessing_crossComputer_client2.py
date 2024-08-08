from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue')

m = QueueManager(address=('10.2.1.3', 30030), authkey=b'dongfuguo')
m.connect()
q = m.get_queue()

for i in range(3):
    print(q.get())
