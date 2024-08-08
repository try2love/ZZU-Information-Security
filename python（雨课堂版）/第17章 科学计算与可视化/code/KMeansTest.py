from numpy import array
from random import randrange
from sklearn.cluster import KMeans

# 获取模拟数据
X = array([[1,1,1,1,1,1,1],
           [2,3,2,2,2,2,2],
           [3,2,3,3,3,3,3],
           [1,2,1,2,2,1,2],
           [2,1,3,3,3,2,1],
           [6,2,30,3,33,2,71]])

# 训练
kmeansPredicter = KMeans(n_clusters=3).fit(X)
# 原始数据分类
category = kmeansPredicter.predict(X)
print('分类情况：', category)
print('='*30)

def predict(element):
    result = kmeansPredicter.predict(element)
    print('预测结果：', result)
    print('相似元素：\n', X[category==result])

# 测试
predict([[1,2,3,3,1,3,1]])
print('='*30)
predict([[5,2,23,2,21,5,51]])


##markers = '.,ov^<>12348sp*hH+xDd|_PX'
##for i, clusters in enumerate((1, 2, 3, 4), start=1):
##    y = KMeans(n_clusters=clusters).fit_predict(X)
##    print(y)
##    plt.subplot(2,2,i)
##    for i in range(clusters):
##        plt.scatter(X[y==i][:, 0], X[y==i][:, 1], marker=markers[i], color=(random(),random(),random()))
##plt.show()
