from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import time
from requests import post
url = "http://owenserver.us.to:23654"


class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Im always thinking about you".encode())
        com = "set:hallLightOn=1;"
        post(url = url, data = {"content":com})
        
def run():
    print("Starting server...")
    server_address = ("", 23653)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("server started!")
    httpd.serve_forever()

run()
