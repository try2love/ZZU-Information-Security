from random import choice, randrange

def catchMe(n=5, maxStep=10):
    '''模拟抓小狐狸，一共n个洞口，允许抓maxStep次
       如果失败，小狐狸就会跳到隔壁洞口'''
    # n个洞口，有狐狸为1，没有狐狸为0
    positions = [0] * n
    # 狐狸的随机初始位置
    oldPos = randrange(0, n)
    positions[oldPos] = 1
    
    # 抓maxStep次
    while maxStep >= 0:
        maxStep -= 1
        # 这个循环保证用户输入是有效洞口编号
        while True:
            try:
                x = input('你今天打算打开哪个洞口呀？（0-{0}）：'.format(n-1))
                # 如果输入的不是数字，就会跳转到except部分
                x = int(x)
                # 如果输入的洞口有效，结束这个循环，否则就继续输入
                assert 0 <= x < n, '要按套路来啊，再给你一次机会。'
                break
            except:
                #如果输入的不是数字，就执行这里的代码
                print('要按套路来啊，再给你一次机会。')
                
        if positions[x] == 1:
            print('成功，我抓到小狐狸啦。')
            break
        else:
            print('今天又没抓到。')
            print(positions)
            
        # 如果这次没抓到，狐狸就跳到隔壁洞口
        if oldPos == n-1:
            newPos = oldPos -1
        elif oldPos == 0:
            newPos = oldPos + 1
        else:
            newPos = oldPos + choice((-1, 1))
        positions[oldPos], positions[newPos] = 0, 1
        oldPos = newPos
    else:
        print('放弃吧，你这样乱试是没有希望的。')

# 启动游戏，开始抓狐狸吧
catchMe()
