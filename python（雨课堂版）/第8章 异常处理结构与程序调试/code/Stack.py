'''
Author: 董付国
email: dongfuguo2005@126.com
Date: 2014-11-10, Updated on 2017-4-1
'''

class Stack:
    def __init__(self, size = 10):
        #使用列表存放栈的元素
        self._content = []
        #初始栈大小
        self._size = size
        #栈中元素个数初始化为0
        self._current = 0
        
    def empty(self):
        #清空栈
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        return not self._content

    def setSize(self, size):
        #如果缩小空间时指定的新大小，小于已有元素个数
        #则删除指定大小之后的已有元素
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size
    
    def isFull(self):
        return self._current == self._size
        
    def push(self, v):
        #模拟入栈，需要先测试栈是否已满
        if self._current < self._size:
            self._content.append(v)
            #栈中元素个数加1
            self._current = self._current+1
        else:
            print('Stack Full!')
            
    def pop(self):
        #模拟出栈，需要先测试栈是否为空
        if self._content:
            #栈中元素个数减1
            self._current = self._current-1
            return self._content.pop()
        else:
            print('Stack is empty!')
            
    def show(self):
        print(self._content)

    def showRemainderSpace(self):
        print('Stack can still PUSH ', self._size-self._current, ' elements.')

if __name__ == '__main__':
    print('Please use me as a module.')
