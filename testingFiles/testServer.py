import requests
import sys
arg = str(sys.argv[1])
print(arg)
r = requests.get(url = "http://owenserver.us.to:23655", data= {'content':arg})
print(r.text)
