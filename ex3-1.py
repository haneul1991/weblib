from urllib.parse import urlparse

result = urlparse("http://www.python.org:80/guido/python.html?name=둘리&id=dooley")
print(result)