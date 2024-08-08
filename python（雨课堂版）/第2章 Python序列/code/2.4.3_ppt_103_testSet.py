import random
import time
def RandomNumbers(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    n = 0
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
            n += 1
        if n == number:
            break
        
    return data

def RandomNumbers1(number, start, end):
    '''使用列表来生成number个介于start和end之间的不重复随机数'''
    data = []
    while True:
        element = random.randint(start, end)
        if element not in data:
            data.append(element)
        if len(data) == number:
            break
        
    return data

def RandomNumbers2(number, start, end):
    '''使用集合来生成number个介于start和end之间的不重复随机数'''
    data = set()
    while True:
        data.add(random.randint(start, end))
        if len(data) == number:
            break

    return data

# 数字范围
begin, end = 1, 100000
# 要获取的不重复数字个数
num = 5000
# 重复测试次数
rep = 10
for ran in (RandomNumbers,RandomNumbers1,RandomNumbers2):
    start = time.time()
    for i in range(rep):
        ran(num, begin, end)
    print(ran.__name__, time.time()-start)
