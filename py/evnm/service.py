#!/usr/bin/python
from http.server import (
    HTTPServer,
    BaseHTTPRequestHandler
)

class FSService(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)

        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # Send message back to client
        message = "Hello world!"
        # Write content as utf-8 data
        self.wfile.write(bytes(message, "utf8"))
        return

def run_server():
    print('starting server...')

    server_address = ('127.0.0.1', 9090)
    httpd = HTTPServer(server_address, FSService)
    print('running server...')
    httpd.serve_forever()

run_server()