from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import time
import random
from requests import post
url = "http://owenserver.us.to:23654"

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        tf = open("diyaWeb","r")
        web = tf.read()
        tf.close()
        self.send_header("content-type", "text/html")
        self.end_headers()
        r1 = random.randint(0,0)
        if r1 == 0:
            #self.wfile.write("Im always thinking about you".encode())
            self.wfile.write(web.encode())
        if r1 == 1:
            self.wfile.write("You look beautiful today Diya<3".encode())
        if r1 == 2:
            self.wfile.write("I cant wait until you are in my arms again".encode())
        com = "set:hallLightOn=1;"
        post(url = url, data = {"content":com})
        
def run():
    print("Starting server...")
    server_address = ("", 23653)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("server started!")
    httpd.serve_forever()

run()
