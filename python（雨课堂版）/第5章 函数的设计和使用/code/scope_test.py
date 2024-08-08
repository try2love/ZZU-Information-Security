def scope_test():
    def do_local():
        spam = "我是局部变量"

    def do_nonlocal():
        nonlocal spam
        #这时要求spam必须是已存在的变量
        spam = "我不是局部变量，也不是全局变量"

    def do_global():
        global spam
        #如果全局作用域内没有spam，就自动新建一个
        spam = "我是全局变量"

    spam = "原来的值"
    do_local()
    print("局部变量赋值后：", spam)
    do_nonlocal()
    print("nonlocal变量赋值后：", spam)
    do_global()
    print("全局变量赋值后：", spam)

scope_test()
print("全局变量：", spam)
