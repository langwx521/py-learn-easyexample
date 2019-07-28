import urllib.request

request = urllib.request.urlopen("http://www.baidu.com")

# print(request.read().decode('utf-8'))

print(request.read())