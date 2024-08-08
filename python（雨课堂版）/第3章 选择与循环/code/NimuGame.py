from random import randint

def nimu(n):
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
        # 计算机玩家随机拿走一些
        n -= randint(1, n//2)            
    else:
        return 'You fail.'
        
print(nimu(randint(1, 100)))
