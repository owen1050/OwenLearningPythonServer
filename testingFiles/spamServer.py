import requests
import sys
import time
arg = str(sys.argv[1])
print(arg)
a = 0
t0 = time.time()
tt=0
num = 1000
while a<num:
    a = a + 1
    tl = time.time()
    r = requests.post(url = "http://owenserver.us.to:23654", data= {'content':arg})
    tt = tt + abs(time.time()-tl)
    #while abs(time.time() - tl)<0.0:
     #   time.sleep(0.01)
print(r.text)
print(tt/num)
