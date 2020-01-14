import requests
kv={'q':'python'}
url='http://www.so.com/s'
try:
    r=requests.get(url,params=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text)
except:
    print('爬虫失败')
#一堆乱码
'''
r=requests.get(url,params=kv)
r.encoding=r.apparent_encoding
print(r.request.url)
#莫名其妙 的百度的搜索关键词这样用不行
'''