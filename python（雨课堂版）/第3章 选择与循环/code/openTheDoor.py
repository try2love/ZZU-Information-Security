from random import randrange

def init():
    '''返回一个字典，键为3个门号，值为门后面的物品'''
    result = {i: 'goat' for i in range(3)}
    r = randrange(3)
    result[r] = 'car'
    return result

def startGame():
    # 获取本次游戏中每个门的情况
    doors = init()
    # 获取玩家选择的门号
    while True:
        try:
            firstDoorNum = int(input('Choose a door to open:'))
            assert 0<= firstDoorNum <=2
            break
        except:
            print('Door number must be between {} and {}'.format(0, 2))
    # 主持人查看另外两个门后的物品情况
    for door in doors.keys()-{firstDoorNum}:
        # 打开其中一个后面为山羊的门
        if doors[door] == 'goat':
            print('"goat" behind the door', door)
            # 获取第三个门号，让玩家纠结
            thirdDoor = (doors.keys()-{door, firstDoorNum}).pop()
            change = input('Do you want to switch to {}?(y/n)'.format(thirdDoor))
            finalDoorNum = thirdDoor if change=='y' else firstDoorNum
            if doors[finalDoorNum] == 'goat':
                return 'I Win!'
            else:
                return 'You Win.'

while True:
    print('='*30)
    print(startGame())
    r = input('Do you want to try once more?(y/n)')
    if r == 'n':
        break
