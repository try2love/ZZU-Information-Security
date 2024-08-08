def before(func):                       #定义修饰器
    def wrapper(*args, **kwargs):
        print('Before function called.')
        return func(*args, **kwargs)
    return wrapper

def after(func):                        #定义修饰器
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('After function called.')
        #return result
    return wrapper

#@before
@after
def test():                             #同时使用两个修饰器改造函数
    print(3)

test()                                  #调用被修饰的函数

