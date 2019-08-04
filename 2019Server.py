
from http.server import BaseHTTPRequestHandler, HTTPServer
 
# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    prevSentString = ""
    
    def do_POST(self):
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        f = open("data.txt", "r+")
        fileCont = f.read()
        f.close()
        f = open("data.txt", "w")
        
        cL = int(self.headers['content-length'])
        inData = self.rfile.read(cL)
        inData = inData.decode()
        
        
        retString = "No Action"

        if "return_if_changed" in inData:
            if prevSentString == inData:
                retString = "no_change"
            else:
                retString = fileCont
        if "set:" in inData:
            lowVI = 4
            highVI =int(inData.find("=")) 
            varToChange = inData[lowVI:highVI]
            lowVI = highVI+1
            highVI = int(inData.find(";"))
            toValue = int(inData[lowVI:highVI]
            if varToChange in fileCont:
                
            else:
                retString = "var not known, use add:[var]=[value] to add
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        f.write(fileCont)
        f.close()
        
        self.wfile.write(retString.encode())
        return
 
def run():
    print('starting server...')
 
  
    server_address = ('',23654)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
  
    try:
        httpd.serve_forever()
    except:
        httpd.shutdown()
        print("Shutdown server")
 
run()
