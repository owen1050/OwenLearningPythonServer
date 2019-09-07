from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib
import os
import time
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
        logF = open("logs.txt", "a+")
        reqCount = reqCount + 1
        print("//////////////////////////////\nRequestNumber:"+ str(reqCount))
        logF.write("=============================\nRequestNumber:"+str(reqCount)+"\n")
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
        print("POST Request:"+inData)
        logF.write("Request:"+inData+"\n")
        retString = "No Action"

        if "sch:" in inData:
            
            lowVI = inData.find("sch:")+4
            highVI = int(inData.find("@"))
            comToDo = inData[lowVI:highVI]
            lowVI = int(highVI + 1)
            highVI = int(inData.find(";", lowVI))
            timeInt = int(inData[lowVI:highVI])
            retString = "Scheduled "+comToDo+" at "+str(timeInt)
            inData = ""
            scFile = open("timeExec.txt", "a+")
            
            minute = int(timeInt % 100)
            hour = int((timeInt - minute)/100)
            scFile.write("time~["+str(hour)+":"+str(minute)+"]="+comToDo + "?")
            scFile.close()

        if "return_if_changed" in inData:
            if prevSentString == fileCont:
                retString = "no_change"
            else:
                retString = fileCont
                prevSentString = fileCont
        if "sudo_reset" in inData:
            p = open("perm.txt", "r+")
            retString = "reset data to default"
            fileCont = p.read()
            p.close()

        if "sudo_reboot" in inData:
            passw = "adminadmin"
            com = "reboot"
            p = os.system("echo %s|sudo -S %s" %(passw, com))
        

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
            print("multipleChangeFound")
            lowVI = inData.find("multipleChange:")+15
            highVI =int(inData.find("=", lowVI)) 
            varToChange = inData[lowVI:highVI]
            lowVI = highVI+1
            highVI = int(inData.find(";"))
            toValue = int(inData[lowVI:highVI])
            if varToChange == "bothLights":
                if toValue == 1:
                    fileCont = setVar(fileCont, "mainLightOn", 1)
                    fileCont = setVar(fileCont, "hallLightOn", 1)
                if toValue == 0:
                    fileCont = setVar(fileCont, "mainLightOff", 1)
                    fileCont = setVar(fileCont, "hallLightOff", 1)
            
            if varToChange == "goodMorning":
                fileCont = setVar(fileCont, "mainLightOn", 1)
                fileCont = setVar(fileCont, "hallLightOn", 1)
                fileCont = setVar(fileCont, "blindsMoveAllUp", 1)

            if varToChange == "goodnight":
                fileCont = setVar(fileCont, "mainLightOff", 1)
                fileCont = setVar(fileCont, "hallLightOff", 1)
                fileCont = setVar(fileCont, "blindMoveAllDown", 1)
            
            if varToChange == "set_projector":
                fileCont = setVar(fileCont, "mainLightOff", 1)
                fileCont = setVar(fileCont, "hallLightOff", 1)
                fileCont = setVar(fileCont, "blindMoveAllDown", 1)
                fileCont = setVar(fileCont, "speakerInProj", 1)
                fileCont = setVar(fileCont, "projectorOn", 1)

            if varToChange == "set_tv":
                fileCont = setVar(fileCont, "mainLightOff", 1)
                fileCont = setVar(fileCont, "hallLightOff", 1)
                fileCont = setVar(fileCont, "blindMoveAllDown", 1)
                fileCont = setVar(fileCont, "speakerInTV", 1)
                fileCont = setVar(fileCont, "tvOn", 1)
      
            
            retString = "Changed all vars asscoiated with " + varToChange
        if "help" in inData:
            h = open("help.txt", "r+")
            retString = h.read()
            h.close()
        
        if "return_all" in inData:
            retString = fileCont
                   
        f.write(fileCont)
        f.close()
        print("Returned:" + retString)
        logF.write("Returned:"+retString+"\n")
        logF.write(str(time.time())+"\n")
        logF.close()
        rq = open("reqCount.txt", "w+")
        rq.write(str(reqCount))
        rq.close()
        
        self.wfile.write(retString.encode())
        return
 
def getVar(s, var):
    vStartI = s.find(var)
    lowVI = 1 + s.find("=", vStartI)
    highVI = s.find("!", lowVI)
    return int(s[lowVI:highVI])

def setVar(s,var, val):
    vStartI = s.find(var)
    lowVI = s.find("=", vStartI)
    highVI = s.find("!", lowVI)
    a = s[:lowVI+1]+str(val)+s[highVI:]
    return a

def run():
    global prevSentString, reqCount
    print('starting server...')
    prevSentString = ""     
    rq = open("reqCount.txt","r")     
    reqCount = int(rq.read())     
    rq.close()     
    p = open("perm.txt", "r+")     
    d = open("data.txt","w+")     
    d.write(p.read())     
    p.close()     
    d.read()     
    server_address = ('',23654)     
    httpd = HTTPServer(server_address, testHTTPServer_RequestHandler)     
    print('running server...')        
    try:         
        httpd.serve_forever()     
    except:         
        httpd.shutdown()         
        print("Shutdown server")          
run()    

