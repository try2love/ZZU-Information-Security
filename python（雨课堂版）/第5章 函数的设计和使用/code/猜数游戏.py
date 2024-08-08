## 系统随机产生一个数，玩家最多可以猜5次，系统会根据玩家的猜测进行提示，
#  玩家则可以根据系统的提示对下一次的猜测进行适当调整。
##

from random import randint

def guess(start=1, end=10, maxTimes=5):
    # 随机生成一个整数
    value = randint(start, end)

    for i in range(maxTimes):
        prompt = '开始猜:' if i==0 else '再猜一次:'
        # 使用异常处理结构，防止输入不是数字的情况
        try:
            x = int(input(prompt))
        except:
            print('不要浪费机会啊，必须输入{0}到{1}之间的数字'.format(start, end))
        else:
            # 猜对了
            if x == value:
                print('太牛了，居然猜对了！')
                break
            elif x > value:
                print('真遗憾，猜的太大啦。')
            else:
                print('有点小哦，加油。')
    else:
        # 次数用完还没猜对，游戏结束，提示正确答案
        print('失败，游戏结束！！！')
        print('本次游戏正确的数是：', value)

if __name__ == '__main__':
    guess(50, 100)
