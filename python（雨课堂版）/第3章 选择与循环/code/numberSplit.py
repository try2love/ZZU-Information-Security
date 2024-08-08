import random

def numberSplit(lst, n,threshold):
    '''lst为原始列表，内含若干整数,n为拟分份数
       threshold为各子列表元素之和的最大差值'''
    print('原始列表：', lst)
    length = len(lst)
    p = length // n
    #尽量把原来的lst列表中的数字等分成n份
    partitions = []
    for i in range(n-1):
        partitions.append(lst[i*p:i*p+p])
    else:
        partitions.append(lst[i*p+p:])

    print('初始分组结果：', partitions)
    
    #不停地调整各个子列表中的数字
    #直到n个子列表中数字之和尽量相等
    times = 0
    while times < 1000:
        times += 1
        maxLst = max(partitions, key=sum)
        minLst = min(partitions, key=sum)
        #把大的子列表中最小的元素调整到小的子列表中
        m = min(maxLst)
        i = maxLst.index(m)
        minLst.insert(0, maxLst.pop(i))
        print('第{0}步处理结果：'.format(times), partitions)
        first = sum(partitions[0])
        for item in partitions[1:]:
            if abs(sum(item)-first) > threshold:
                break
        else:
            break
    else:
        print('很抱歉，我无能为力，只能给出这样一个结果了。')
    return partitions

lst = [random.randint(1, 100) for i in range(10)]

result = numberSplit(lst, 3, 15)
print('最终结果：', result)
#输出各组数字之和
print('各子列表元素之和：')
for item in result:
    print(sum(item))
