#GET 방식으로 웹 서버에 요청 보내기
from urllib.parse import urlencode
from urllib.request import urlopen

query = urlencode({'name':'둘리','a':10,'b':20})
f = urlopen('http://www.example.com?'+ query)
body = f.read()
print(body)