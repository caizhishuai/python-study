# encoding:utf-8
import httplib2, urllib3

# get调用

httpClient = None

try:
    httpClient = httplib2.HTTPConnectionWithTimeout("www.ljja.cn", 80, timeout=30)
    httpClient.request("http://www.ljja.cn/","GET",None, {'Content-type': 'application/x-www-form-urlencoded'})
    response = httpClient.getresponse()
    print(response.status)
    print(response.reason)
    print(response.read())
    print(response.getheaders())

except Exception as e:
    print(e)

finally:
    if httpClient:
        httpClient.close()

