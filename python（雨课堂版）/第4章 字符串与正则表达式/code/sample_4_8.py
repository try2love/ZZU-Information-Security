import os
import re
def detectIframe(fn):
    #存放网页文件内容的列表
    content = []
    with open(fn, encoding='utf8') as fp:
        #读取文件所有行，删除两侧的空白字符，然后添加到列表中
        for line in fp:
            content.append(line.strip())
    #把所有内容连接成字符串
    content = ' '.join(content)
    #正则表达式
    m = re.findall(r'<iframe\s+src=.*?></iframe>', content)
    if m:
        #返回文件名和被嵌入的框架
        return {fn:m}
    return False

#遍历当前文件夹中所有html和htm文件并检查是否被嵌入框架
for fn in (f for f in os.listdir('.') if f.endswith(('.html','.htm'))):
    r = detectIframe(fn)
    if not r:
        continue
    #输出检查结果
    for k, v in r.items():
        print(k)
        for vv in v:
            print('\t', vv)

