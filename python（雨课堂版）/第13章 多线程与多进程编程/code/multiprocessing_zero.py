from multiprocessing import Process

class MyProcess(Process):
    def __init__(self):
        Process.__init__(self)

    def run(self):
        print('ok')

if __name__ == '__main__':
    p = MyProcess()
    p.start()
