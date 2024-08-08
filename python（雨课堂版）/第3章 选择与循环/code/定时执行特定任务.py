import datetime
import time

def doSth():
    print('test')
    # 假装做这件事情需要一分钟
    time.sleep(60)

def main(h=0, m=0):
    '''h表示设定的小时，m为设定的分钟'''
    while True:
        # 判断是否达到设定时间，例如0:00
        while True:
            now = datetime.datetime.now()
            # 到达设定时间，结束内循环
            if now.hour==h and now.minute==m:
                break
            # 不到时间就等20秒之后再次检测
            time.sleep(20)
        # 做正事，一天做一次
        doSth()

main(10,14)
