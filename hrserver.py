from http.server import BaseHTTPRequestHandler, HTTPServer

last_hr = 0

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200, "OK")
        self.send_header('Content-type', 'application/json')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        data = "{"+ "\"bpm\":{}".format(last_hr) +"}"
        data = data.encode('utf-8')
        self.wfile.write(data)

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        if("bpm" in self.headers):
            hr = self.headers["bpm"]
            global last_hr
            last_hr = int(hr) if hr.isdigit() else None
            print(last_hr)
        self.send_response(200, "OK")
        self.end_headers()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

def run(server_class=HTTPServer, handler_class=S, port=7575):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()

if __name__ == '__main__':
    from sys import argv
    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()