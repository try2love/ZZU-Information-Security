from multiprocessing.managers import BaseManager
from queue import Queue

q = Queue()
class QueueManager(BaseManager):
    pass
QueueManager.register('get_queue', callable=lambda:q)

m = QueueManager(address=('', 30030), authkey=b'dongfuguo')
s = m.get_server()
s.serve_forever()
