import random

def init():
    # 初始状态，每个格内都是1-9之间的数字
    grids = {(r, c):list(range(1,10))\
             for r in range(9) for c in range(9)}
    
    # 根据文件中的位置和数字设置数独游戏初始状态
    with open('values.txt') as fp:
        for line in fp:
            line = line.strip()
            if line == '0':
                break
            row, col, value = map(int, line.split(','))
            grids[(row,col)] = value
    return grids

def eachGrid(grids, row, col, value):
    tempValue = grids[(row,col)]
    # 删除不可能的数字
    if isinstance(tempValue, list):
        if value in tempValue:
            tempValue.remove(value)
        # 如果格内只有一个数字，就拿出来填充
        if len(tempValue) == 1:
            grids[(row,col)] = tempValue[0]

def solve(oldGrids):
    grids = oldGrids.copy()
    for r in range(9):
        for c in range(9):
            value = grids[(r,c)]
            if isinstance(value, int):
                # 处理同一列
                for rr in range(9):
                    eachGrid(grids, rr, c, value)
                # 处理同一行
                for cc in range(9):
                    eachGrid(grids, r, cc, value)
                # 处理小九宫格内的数字
                rowStart = r//3 * 3
                colStart = c//3 * 3
                for rr in range(rowStart, rowStart+3):
                    for cc in range(colStart, colStart+3):
                        eachGrid(grids, rr, cc, value)
            elif isinstance(value, list) and len(value)==1:
                # 当前格内只有一个数了，拿出来
                grids[(r,c)] = value[0]
    return grids

def output(grids):
    '''输出grids中的内容'''
    for row in range(9):
        for col in range(9):
            value = grids[(row,col)]
            if isinstance(value, int):
                print(grids[(row,col)], end=' ')
            else:
                print(' ', end=' ')
        print()

def check(grids):
    '''检查grids是否满足数独游戏要求'''
    for rc in range(9):
        row = {grids[(rc,c)] for c in range(9)}
        if len(row) != 9:
            return False
        col = {grids[(r,rc)] for r in range(9)}
        if len(col) != 9:
            return False
    for row in range(0,9,3):
        for col in range(0,9,3):
            value = {grids[(r,c)]\
                     for r in range(row,row+3)\
                     for c in range(col,col+3)}
            if len(value) != 9:
                return False
    return True

def main(oldGrids):
    grids = oldGrids.copy()
    steps = 0
    while True:
        steps += 1
        grids = solve(grids)
        if steps > 20:
            try:
                position = [(r,c)\
                            for r in range(9) for c in range(9)\
                            if isinstance(grids[(r,c)],list)][0]
                grids[position] = random.choice(grids[position])
            except:
                grids = oldGrids.copy()
                steps = 0
                continue
        
        if all({isinstance(grids[(r,c)], int)\
                for r in range(9) for c in range(9)}):
            if check(grids):
                return grids
            else:
                # 当前选择无效，恢复原状，选择下一个
                grids = oldGrids.copy()
                print(steps)
                steps = 0
                
grids = init()
output(grids)
result = main(grids)
print('='*30)
output(result)
print(check(result))
