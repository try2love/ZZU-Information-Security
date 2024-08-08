from random import randrange

# 其他用户喜欢看的电影清单
data = {'user'+str(i):{'film'+str(randrange(1, 10)) for j in range(randrange(15))} for i in range(10)}

# 待测用户曾经看过并感觉不错的电影
user = {'film1', 'film2', 'film3'}
# 查找与待测用户最相似的用户和Ta喜欢看的电影
similarUser, films = max(data.items(),key=lambda item: len(item[1]&user))

print('历史数据：')
for u, f in data.items():
    print(u, f, sep=':')

print('和您最相似的用户是：', similarUser)
print('Ta最喜欢看的电影是：', films)
print('Ta看过的电影中您还没看过的有：', films-user)
