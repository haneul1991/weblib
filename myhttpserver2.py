from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs

port = 7777

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def get_params(self, name):
        qs = self.path[self.path.find('?')+1:]
        params = parse_qs(qs)
        values = params.get(name)

        return '' if values is None else values.pop()

    def ex1(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요</h1>'.encode('utf-8'))

    def ex2(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요2</h1>'.encode('utf-8'))

        '''if values is None:
            return None
        else:
            return values.pop()'''

    def do_GET(self):
        index = self.path.find('?')
        req_url = self.path if index == -1 else self.path[:index]

        # URL Mapping
        if req_url == '/iot':
            handler_name = 'ex' + self.get_params('ex')
            # print(handler_name)
            if handler_name not in MyHTTPRequestHandler.__dict__:
                self.send_error(404, 'File Not Found')
                return

            MyHTTPRequestHandler.__dict__[handler_name](self)


        elif req_url == '/board':
            pass
        else:
            self.send_error(404, 'File Not Found')


httpd = HTTPServer(('', port), MyHTTPRequestHandler)
print('Server running on port', port)
httpd.serve_forever()