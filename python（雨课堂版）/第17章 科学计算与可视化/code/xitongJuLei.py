from random import randrange

def generate(s, m1, m2):
    '''生成形式如[('a',(1,5)), ('b', (3,6))]的随机坐标'''
    x = [(ch, (randrange(m1), randrange(m2)))
         for ch in s]
    return x

def xitongJulei(points, k=5):
    '''根据欧几里得距离对points进行聚类，最终划分为k类'''
    points = points[:]
    while len(points)>k:
        nearest = float('inf')
        # 查找距离最近的两个点，进行合并
        # 合并后的两个点，使用中点代替其坐标
        for index1, point1 in enumerate(points[:-1]):
            position1 = point1[1]
            # 注意：这里的start参数很重要
            for index2, point2 in enumerate(points[index1+1:], start=index1+1):
                  position2 = point2[1]
                  distance = (position1[0]-position2[0])**2 + (position1[1]-position2[1])**2
                  if distance < nearest:
                      result = (index1, index2)
                      nearest = distance
        # 弹出距离最近的两个点，合并为一个点
        p2 = points.pop(result[1])
        p1 = points.pop(result[0])
        p = (p1[0]+p2[0], ((p1[1][0]+p2[1][0])/2, (p1[1][1]+p2[1][1])/2))
        # 使用合并后的点代替原来的两个点
        points.append(p)
        # 查看每步处理后的数据
        print(points)
    return points

points = generate('abcde', 5, 5)
print('origin:'.center(20,'=')+'\n', points)
print('steps:'.center(20,'='))
result = xitongJulei(points, k=2)
print('result'.center(20,'='))
print(result)
