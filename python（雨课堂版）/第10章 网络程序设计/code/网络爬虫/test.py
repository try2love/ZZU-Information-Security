# -*- coding: cp936 -*-
import WebCrawler

url = input('�������url(��-->http://www.baidu.com): \n')
thNumber = int(input('�����߳���:'))    #֮ǰ����δת����bug

wc = WebCrawler.WebCrawler(thNumber)
wc.Craw(url)
