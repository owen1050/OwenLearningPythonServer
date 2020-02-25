from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import time
import random
from requests import post
from requests import get
url = "http://owenserver.us.to:23654"

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
     
        
        tf = open("23653HTML","r")
        web = tf.read()
        tf.close()
    
        
        self.send_response(200)
        self.end_headers()
        self.wfile.write(web.encode())
        

def run():
    print("Starting server...")
    server_address = ("", 23653)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("server started!")
    httpd.serve_forever()

run()
