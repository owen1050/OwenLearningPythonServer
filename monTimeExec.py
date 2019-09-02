import time
import datetime
from requests import post
import pytz

url = "http://owenserver.us.to:23654"
fmt = "%H:%M"
est = pytz.timezone("US/Eastern") 
tf = open("bootTimes.txt", "a+")
tf.write(str(datetime.datetime.now()))
tf.close()

while True:
    f = open("timeExec.txt", "r")
    et = f.read()
    f.close()
    oldET = et
    startI = 0
    while "time~" in et[startI:]:
        eHLI = et.find("[",startI)+1
        eHHI = et.find(":", eHLI)
        eH = int(et[eHLI:eHHI])
        eMLI = eHHI+1
        eMHI = et.find("]", eMLI)
        eM = int(et[eMLI:eMHI])

        tt = datetime.datetime.now().astimezone(est).strftime(fmt)
        tH = int(tt[0:tt.find(":")])
        tM = int(tt[tt.find(":")+1:])
        eLI = eMHI+2
        eHI = et.find("?", eLI)
        if eH == tH and eM == tM:
            com = et[eLI:eHI]           
            et = et[0:eHLI-6]+et[eHI+1:]
            f = open("timeExec.txt", "w")
            f.write(et)
            f.close()
            print(com) 
            print(et)
            post(url = url, data = {"content":com})
        else:
         
            startI = eHI
        print(eH, eM, tH, tM)
    
    time.sleep(1)
