import timeit
strlist = ['This is a long string that will not keep in memory.' for n in range(10000)]

def use_join():
    return ''.join(strlist)

def use_plus():
    result = ''
    for strtemp in strlist:
        result = result+strtemp
    return result


#重复运行次数
times = 1000
jointimer = timeit.Timer('use_join()', 'from __main__ import use_join')
print('time for join:', jointimer.timeit(number=times))
plustimer = timeit.Timer('use_plus()', 'from __main__ import use_plus')
print('time for plus:', plustimer.timeit(number=times))

