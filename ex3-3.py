#POST 방식으로 웹 서버에 요청 보내기
from urllib.parse import urlencode
from urllib.request import Request, urlopen

data = urlencode({'name':'둘리','email':'','pwd':''}) #join페이지에서 이부분에 빈공간으로 하고 for문을 돌리면 자동회원가입이 된다.
data = data.encode('UTF-8')

request = Request('http://www.example.com/join', data)
request.add_header('Content-Type', 'text/html')

f = urlopen(request)
response = f.read()
print(response)
