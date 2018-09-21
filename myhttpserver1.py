from http.server import BaseHTTPRequestHandler, HTTPServer

port = 9999

class MyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>안녕하세요</h1>'.encode('utf-8'))


httpd = HTTPServer(('', 9999), MyHTTPRequestHandler)
print('Server running on port', 9999)
httpd.serve_forever()