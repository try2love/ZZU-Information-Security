from math import log2
from random import randint

def everyStep(n):
    num = n - (2**int(log2(n))-1)
    half = n // 2
    # 让剩余物品数量为2的幂次方减1
    if num <= half:
        return num
    # 如果实在没有办法，就随机拿走一些
    return randint(1, half)

def smartNimuGame(n):
    while n > 1:
        # 人类玩家先走
        print("Now it's your turn, and we have {0} left.".format(n))
        # 确保人类玩家输入合法整数值
        while True:
            try:
                num = int(input('How many do you want to take:'))
                assert 1 <= num <= n//2
                break
            except:
                print('The num you can take must be between 1 and {0}'.format(n//2))
        n -= num
        if n == 1:
            return 'I fail.'
        # 计算机玩家拿走一些
        n -= everyStep(n)            
    else:
        return 'You fail.'

print(smartNimuGame(randint(1, 100)))
