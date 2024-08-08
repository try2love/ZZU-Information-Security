import math

critics={
'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5,'The Night Listener': 3.0},

'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5,'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0,'You, Me and Dupree': 3.5},

'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0, 'Superman Returns':4.0}
}


def sim_distance(prefs,person1,person2):
    # 得到共同的电影
    si={}
    for item in prefs[person1]:
        if item in prefs[person2]:
            si[item]=1
    
    # 如果没有共同的电影则返回0
    if len(si)==0: return 0
    #计算欧几里得距离，返回相似度 
    sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) for item in prefs[person1] if item in prefs[person2]])
    return 1/(1+sum_of_squares)



def sim_pearson(prefs,p1,p2):
    # 得到共同评价的电影
    si={}
    for item in prefs[p1]:
        if item in prefs[p2]: si[item]=1
            
    # 如果没有共同评价的电影，返回0
    if len(si)==0: return 0
    
    # 将两人的偏好相加
    sum1=sum([prefs[p1][it] for it in si])
    sum2=sum([prefs[p2][it] for it in si])
    # 计算平方和
    sum1Sq=sum([pow(prefs[p1][it],2) for it in si])
    sum2Sq=sum([pow(prefs[p2][it],2) for it in si])
    # 计算对应项的乘积和
    pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
    # 计算皮尔逊相关度
    n=len(si)
    num=pSum-(sum1*sum2/n)
    den=math.sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
    if den==0: return 0
    r=num/den
    return r


def topMatches(prefs,person,n=5,similarity=sim_pearson):
    scores=[(similarity(prefs,person,other),other)
    for other in prefs if other!=person]
    # 对list排序，相似度最高的人排在最前
    scores.sort( )
    scores.reverse( )
    return scores[0:n]


def getRecommendations(prefs,person,similarity=sim_pearson):
    totals={}
    simSums={}
    for other in prefs:
        # 不和自己比
        if other==person: continue
        sim=similarity(prefs,person,other)
        # 忽略小于等于0的评分
        if sim<=0: continue
        for item in prefs[other]:
            # 只计算我没看过的电影
            if item not in prefs[person] or prefs[person][item]==0:
                # 相似度乘以得分
                totals.setdefault(item,0)
                totals[item]+=prefs[other][item]*sim
                # 相似度求和
                simSums.setdefault(item,0)
                simSums[item]+=sim
    # 对结果进行归一化
    rankings=[(total/simSums[item],item) for item,total in totals.items( )]
    # 排序并返回结果
    rankings.sort( )
    rankings.reverse( )
    return rankings


print(sim_distance(critics, 'Lisa Rose','Gene Seymour'))

print(sim_pearson(critics,'Lisa Rose','Gene Seymour'))

getRecommendations(critics,'Toby',similarity=sim_distance)