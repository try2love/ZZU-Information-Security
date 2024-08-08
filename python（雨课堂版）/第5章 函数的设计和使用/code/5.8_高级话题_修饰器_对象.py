def check_permission(func):
    def wrapper(*args, **kwargs):
        if kwargs.get('username')!='admin':
            raise Exception('Sorry. You are not allowed.')
        print(args,kwargs)
        return func(*args, **kwargs)
    return wrapper
                     
class ReadWriteFile(object):
    #把函数check_permission作为装饰器使用
    @check_permission
    def read(self, username, filename):
        return open(filename,'r').read()

    def write(self, username, filename, content):
        open(filename,'a+').write(content)
    #把函数check_permission作为普通函数使用
    write = check_permission(write)
                    

t = ReadWriteFile()
print('Originally.......')
print(t.read(username='admin', filename=r'c:\sample2.txt'))
print('Now, try to write to a file........')
t.write(username='admin', filename=r'c:\sample2.txt', content='\nhello world')
print('After calling to write...........')
print(t.read(username='admin', filename=r'c:\sample2.txt'))

