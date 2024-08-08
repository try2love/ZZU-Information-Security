def longest(s):
    result = []
    t = []
    for ch in s:                      # 遍历字符串中所有字符
        if '0'<=ch<='9':              # 遇到数字，记录到临时变量
            t.append(ch)
        elif t:
            result.append(''.join(t)) #遇到非数字，把临时的连续数字记下来
            t = []

    if t:                             # 考虑原字符串以数字结束的情况
        result.append(''.join(t))

    if result:
        return max(result, key=len)

    return 'No'

maxStr=longest("123abs345633sein89-023uio")
print(maxStr)
