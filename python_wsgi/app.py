# -*- coding: utf-8 -*-
from wsgiref.simple_server import make_server

def application(environ, start_response):
    status = '200 OK'
    headers = [('Content-type', 'text/plain; charset=utf-8')]
    start_response(status, headers)

    response_body = b'Hello from Python WSGI Application!'
    return [response_body]

if __name__ == '__main__':
    print("Starting server on port 8082...")
    with make_server('0.0.0.0', 8082, application) as httpd:
        print("Server is running on port 8082...")
        httpd.serve_forever()
