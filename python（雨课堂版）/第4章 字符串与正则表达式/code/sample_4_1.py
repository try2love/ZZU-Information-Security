def crypt(source, key):
    from itertools import cycle
    result = ''
    temp = cycle(key)
    for ch in source:
        result = result + chr(ord(ch) ^ ord(next(temp)))
    return result

source = 'Shandong Institute of Business and Technology'
key = 'Dong Fuguo'

print('Before Encrypted:'+source)
encrypted = crypt(source, key)
print('After Encrypted:'+encrypted)
decrypted = crypt(encrypted, key)
print('After Decrypted:'+decrypted)
