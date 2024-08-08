from random import randrange
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf

def generateData(startDate, endDate):
    df = pd.DataFrame([300+i*30+randrange(50) for i in range(31)],\
                      columns=['营业额'],\
                      index=pd.date_range(startDate, endDate, freq='D'))
    return df

# 生成测试数据
data = generateData('20170601', '20170701')
print(data)
# 绘制时序图
myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\Arial.ttf')
##myfont = fm.FontProperties(fname=r'C:\Windows\Fonts\STKAITI.ttf')
data.plot()
plt.legend(prop=myfont)  
plt.show()
# 生成自相关图
plot_acf(data).show()
# 生成偏自相关图
plot_pacf(data).show()
