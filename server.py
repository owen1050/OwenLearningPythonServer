
#!/usr/bin/env python
"""
Very simple HTTP server in python.
Usage::
    ./dummy-web-server.py [<port>]
Send a GET request::
    curl http://localhost
Send a HEAD request::
    curl -I http://localhost
Send a POST request::
    curl -d "foo=bar&bin=baz" http://localhost
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
import SocketServer
from termcolor import colored
data = " "
class S(BaseHTTPRequestHandler):
    
    
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        file1 = open("data.txt", "r")
        self._set_headers()
        data = file1.read()
        file1.close() 
                
        first = data.find("!")
        second = data.find("!", first+1)
        data = data[first:second+1]

        file1 = open("data.txt", "w")
        file1.write(data)
        self.wfile.write(data)
        file1.close() 
        print(data)
    def do_HEAD(self):
        self._set_headers()
        
    def do_POST(self):
        
        file1 = open("data.txt", "r")
                      
        data = file1.read()
        first = data.find("!")
        second = data.find("!", first+1)
        data = data[first:second+1]
        file1.close()
        
        

        lengthOfIncomingData = int(self.headers['Content-Length'])
        incomingData = self.rfile.read(lengthOfIncomingData)
        print(colored(incomingData,'yellow'))
        paramToLookFor = incomingData[0:incomingData.find("=")]
        newValueOfParam = incomingData[incomingData.find("="): incomingData.find(";")]
        
        indexOfData = data.find(paramToLookFor)+len(paramToLookFor)
        
        if indexOfData-len(paramToLookFor) >= 0:
            data = data[:indexOfData] + newValueOfParam  +data[data.find(";",indexOfData):]
            print(colored("Found param, updating",'yellow')) 
        if incomingData.find("RESET")>=0:
            data = "!BlindState=0;BlindPos=0;!"
            print(colored("RESETING",'red'))
        if incomingData.find("FLIRT")>=0:
            data = "Sam Young is beautiful and brilliant"
            print(colored("INITIATE FLIRTTING",'red'))
                
        if incomingData.find("ADDPARAM")>=0:
            paramToAdd = incomingData[:incomingData.find(";")+1]
            check = paramToAdd[:paramToAdd.find("=")]
            if data.find(check) == -1:
                data = "!" + paramToAdd + data[1:]
                print(colored("ADDED PARAM" + check,'red'))
        
        
        print(colored(data,'red'))
        file1 = open("data.txt", "w")
        file1.write(data)
        self._set_headers()
        self.wfile.write(data)
        file1.close()


def run(server_class=HTTPServer, handler_class=S, port=23654):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print ('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
