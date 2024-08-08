'''
Author: 董付国
部分成果：《Python程序设计基础》、《Python程序设计（第2版）》
          《Python可以这样学》
微信公众号：Python小屋，关注人数12000人，分享文章近500篇
email: dongfuguo2005@126.com
Date: 2014-11-10, Updated on 2017-12-8
'''

class Stack:
    def __init__(self, size = 10):
        '''创建栈对象并进行初始化，默认栈大小为10'''
        # 使用列表存放栈的元素
        self._content = []
        # 初始栈大小
        self._size = size
        # 栈中元素个数初始化为0
        self._current = 0
        
    def empty(self):
        '''清空栈'''
        self._content = []
        self._current = 0
        
    def isEmpty(self):
        '''测试栈是否为空'''
        return not self._content

    def setSize(self, size):
        '''调整栈的大小，可以增大或缩小栈空间'''
        # 如果缩小空间时指定的新大小，小于已有元素个数
        # 则删除指定大小之后的已有元素
        if size < self._current:
            for i in range(size, self._current)[::-1]:
                del self._content[i]
            self._current = size
        self._size = size
    
    def isFull(self):
        '''测试栈是否已满'''
        return self._current == self._size
        
    def push(self, v):
        '''将新元素入栈'''
        # 模拟入栈，需要先测试栈是否已满
        if self._current < self._size:
            self._content.append(v)
            # 栈中元素个数加1
            self._current = self._current+1
        else:
            print('Stack Full!')

    def __str__(self):
        return str(self._content)

    __repr__ = __str__
            
    def pop(self):
        '''将栈顶元素出栈'''
        # 模拟出栈，需要先测试栈是否为空
        if self._content:
            # 栈中元素个数减1
            self._current = self._current-1
            return self._content.pop()
        else:
            print('Stack is empty!')
            
    def show(self):
        '''显示当前栈对象中的元素'''
        print(self._content)

    def showRemainderSpace(self):
        '''显示栈对象剩余空间大小'''
        print('Stack can still PUSH ', self._size-self._current, ' elements.')

if __name__ != '__main__':
    s = '''本模块由董付国编写，仅供学习和参考，
更多资源请关注微信公众号“Python小屋”
或参照《Python程序设计基础》、
      《Python程序设计（第2版）》、
      《Python可以这样学》、《Python程序设计开发宝典》系列图书
或与作者邮箱dongfuguo2005@126.com联系
使用方法：
        from stackDfg import Stack
        s = Stack()
        然后通过dir(s)命令查看详细用法
        并使用help(s.push)之类的命令查看具体用法'''
    print(s)

