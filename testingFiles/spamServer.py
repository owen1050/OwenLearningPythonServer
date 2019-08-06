import requests
import sys
arg = str(sys.argv[1])
print(arg)
a = 0
while a<1000:
    print(a)
    a = a + 1
    r = requests.post(url = "http://owenserver.us.to:23654", data= {'content':arg})
print(r.text)
