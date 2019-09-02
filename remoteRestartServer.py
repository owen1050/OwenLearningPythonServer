from http.server import BaseHTTPRequestHandler, HTTPServer
import threading
import os
import time
from requests import get

class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("Server is restarting, please wait 30 seconds to reconnect".encode())
        pw = "adminadmin"
        com = "reboot"
        p = os.system("echo %s|sudo -S %s" %(pw, com))
def run():
    print("Starting server...")
    server_address = ("", 23655)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print("server started!")
    httpd.serve_forever()

def monIP():
    url = "https://maker.ifttt.com/trigger/monitorip/with/key/Bf91G_MsjKUzsWqRs5N7n"
    oldIp = "100.35.205.75"
    get(url=url, params = dict(value1 = "Computer booted up"))
    while True:
        ip = get('https://api.ipify.org').text
        if ip == oldIp:
            pass
        else:
            print(ip)
            params = dict(value1=str(ip))
            resp = get(url = uel, params = params)
            oldIp = ip
        time.sleep(10)
    
t1 = threading.Thread(target=monIP)
t1.start()
run()
