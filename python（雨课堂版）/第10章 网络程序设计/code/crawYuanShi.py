import re
import os
import os.path
import time
from urllib.request import urlopen

dstDir = 'YuanShi'
if not os.path.isdir(dstDir):
    os.mkdir(dstDir)

startUrl = r'http://www.cae.cn/cae/html/main/col48/column_48_1.html'
with urlopen(startUrl) as fp:
    content = fp.read().decode()

# 提取并遍历每位大牛链接
pattern = r'<li class="name_list"><a href="(.+)" target="_blank">(.+)</a></li>'
result = re.findall(pattern, content)
for item in result:
    perUrl, name = item
    print(perUrl)
    # 这里根据初爬结果进行改进
    name = name.replace('<h3>', '').replace('</h3>', '')
    name = os.path.join(dstDir, name)
    perUrl = r'http://www.cae.cn/' + perUrl
    with urlopen(perUrl) as fp:
        content = fp.read().decode()
    # 别爬太快，休息一下
    time.sleep(0.3)
    # 抓取照片
    pattern = r'<img src="/cae/admin/upload/(.+)" style='
    result = re.findall(pattern, content, re.I)
    if result:
        picUrl = r'http://www.cae.cn/cae/admin/upload/{0}'.format(result[0].replace(' ', r'%20'))
        with open(name+'.jpg', 'wb') as pic:
            pic.write(urlopen(picUrl).read())            
    # 抓取简介
    pattern = r'<p>(.+?)</p>'
    result = re.findall(pattern, content)
    if result:
        intro = re.sub('(<a.+</a>)|(&ensp;)|(&nbsp;)', '', '\n'.join(result))
        with open(name+'.txt', 'w', encoding='utf8') as fp:
            fp.write(intro)
