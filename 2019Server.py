
from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib 

# HTTPRequestHandler class
class testHTTPServer_RequestHandler(BaseHTTPRequestHandler):
    prevSentString = ""
   

    def do_GET(self):
        self.send_response(200)
        self.send_header("content-type", "text/plain")
        self.end_headers()
        self.wfile.write("This is a server up get test".encode())
    def do_POST(self):
        global prevSentString, reqCount
        reqCount = reqCount + 1
        print(reqCount)
        self.send_response(200)
        self.send_header('Content-type','text/plain')
        self.end_headers()
        
        f = open("data.txt", "r+")
        fileCont = f.read()
        f.close()
        f = open("data.txt", "w")
        
        cL = int(self.headers['content-length'])
        inData = self.rfile.read(cL)
        inData = urllib.parse.unquote(str(inData))
        
        retString = "No Action"

        if "return_if_changed" in inData:
            if prevSentString == fileCont:
                retString = "no_change"
            else:
                retString = fileCont
                prevSentString = fileCont
        
        if "set:" in inData:
            lowVI = inData.find("set:")+4
            highVI =int(inData.find("=", lowVI)) 
            varToChange = inData[lowVI:highVI]
            lowVI = highVI+1
            highVI = int(inData.find(";"))
            toValue = int(inData[lowVI:highVI])
            if varToChange in fileCont:
                vStartI = fileCont.find(varToChange)
                lowVI = fileCont.find("=", vStartI)
                highVI = fileCont.find("!", lowVI)
                retString = varToChange + " Changed to " + str(toValue)
                fileCont = fileCont[:lowVI+1] + str(toValue) + fileCont[highVI:]
            else:
                retString = "Var not found, adding: " + varToChange
                fileCont = fileCont + "!" + varToChange + "=" + str(toValue) + "!"
        
            if "multipleChange:" in inData:
                lowVI = inData.find("multipleChanges:")+4
                highVI =int(inData.find("=", lowVI)) 
                varToChange = inData[lowVI:highVI]
                lowVI = highVI+1
                highVI = int(inData.find(";"))
                toValue = int(inData[lowVI:highVI])
                if varToChange == "bothLights":
                    #make fucntion which changes 
        
        f.write(fileCont)
        f.close()
        
        self.wfile.write(retString.encode())
        return
 
def run():
    global prevSentString, reqCount
    print('starting server...')
    prevSentString = ""
    reqCount = 0 
    server_address = ('',23654)
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)
    print('running server...')
  
    try:
        httpd.serve_forever()
    except:
        httpd.shutdown()
        print("Shutdown server")
 
run()
