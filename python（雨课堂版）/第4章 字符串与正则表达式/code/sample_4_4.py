def rev1(s):
    return ' '.join(reversed(s.split()))

def rev2(s):
    t = s.split()
    t.reverse()
    return ' '.join(t)

def rev5(s):
    '''字符串整体逆序，分隔，再各单词逆序'''
    t = ''.join(reversed(s)).split()
    t = map(lambda x:''.join(reversed(x)), t)
    return ' '.join(t)
