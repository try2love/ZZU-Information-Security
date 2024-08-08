import urllib.request
fp = urllib.request.urlopen(r'https://news.sina.com.cn/c/xl/2020-04-29/doc-iirczymi9087377.shtml')
print(fp.read(100))
print(fp.read(100).decode())
fp.close()