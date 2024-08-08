'''问题描述与程序功能：
   编写程序模拟抓狐狸的小游戏。假设一共有一排5个洞口，小狐狸最开始的时候在其中一个洞口，
   然后人随机打开一个洞口，如果里面有小狐狸就抓到了。如果洞口里没有小狐狸就明天再来抓，
   但是第二天小狐狸会在有人来抓之前跳到隔壁洞口里。
   代码主要演示选择结构和循环结构的用法。
'''

from random import choice, randrange

def catchMe(n=5, maxStep=10):
    '''模拟抓小狐狸，一共n个洞口，允许抓maxStep次
       如果失败，小狐狸就会跳到隔壁洞口'''
    # n个洞口，有狐狸为1，没有狐狸为0
    positions = [0] * n
    # 狐狸的随机初始位置
    oldPos = randrange(1, n)
    positions[oldPos] = 1
    
    # 抓maxStep次
    while maxStep >= 0:
        maxStep -= 1
        
        # 这个循环保证用户输入是有效洞口编号
        while True:
            try:
                x = input('你今天打算打开哪个洞口呀？（0-{0}）：'.format(n-1))
                x = int(x)
                if 0 <= x < n:
                    break
                else:
                    print('要按套路来啊，再给你一次机会。')
            except:
                print('要按套路来啊，再给你一次机会。')

        # 如果当前打开的洞口里有小狐狸，就抓到了
        if positions[x] == 1:
            print('成功，我抓到小狐狸啦。')
            break
        else:
            print('今天又没抓到。')
            # 显示每天狐狸的位置，可以删掉下面一行来玩
            print(positions)
            
        # 如果这次没抓到，狐狸就跳到隔壁洞口
        # 已经跳到最右边的洞口了，下次只能往左跳
        if oldPos == n-1:
            newPos = oldPos -1
        # 已经跳到最左边的洞口了，下次只能往右跳
        elif oldPos == 0:
            newPos = oldPos + 1
        # 如果当前仍在几个洞口的中间位置，下次随机选择一个相邻的洞口
        else:
            newPos = oldPos + choice((-1, 1))
            
        # 跳到隔壁洞口
        positions[oldPos], positions[newPos] = positions[newPos], positions[oldPos]
        oldPos = newPos
    else:
        print('放弃吧，你这样乱试是没有希望的。')

# 启动游戏，开始抓小狐狸吧
catchMe()
