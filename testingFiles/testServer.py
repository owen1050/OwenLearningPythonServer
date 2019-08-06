import requests
import sys
arg = str(sys.argv[1])
print(arg)
r = requests.post(url = "http://owenserver.us.to:23654", data= {'content':arg})
print(r.text)
