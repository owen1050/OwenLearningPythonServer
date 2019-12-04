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
        url = "https://maker.ifttt.com/trigger/monitorip/with/key/Bf91G_MsjKUzsWqRs5N7n"
        #get(url=url, params = dict(value1 = "FORTNITE"))        
        
        self.send_response(200)
        tf = open("diyaWeb","r")
        web = tf.read()
        tf.close()

        pic = open("picture.png", "rb")
        picture = pic.read()
        pic.close()
        info = os.stat("picture.png")
        size = info.st_size

        self.send_header("Content-type", "image/jpg")
        self.send_header("Content-length", size)
        self.end_headers()
        r1 = random.randint(0,0)
        r1 = 3
        if r1 == 0:
            #self.wfile.write("Im always thinking about you".encode())
            self.wfile.write(web.encode())
        if r1 == 1:
            self.wfile.write("You look beautiful today Diya<3".encode())
        if r1 == 2:
            self.wfile.write("I cant wait until you are in my arms again".encode())
        if r1 == 3:
            self.wfile.write(picture)
        print(self.path)
        com = "set:hallLightOn=1;"
       # post(url = url, data = {"content":com})
        
def run():
    print("Starting server...")
    server_address = ("", 23653)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("server started!")
    httpd.serve_forever()

run()
