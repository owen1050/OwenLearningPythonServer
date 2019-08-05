import requests
import sys
print(sys.argv[1])
send = str(sys.argv[1])
while True:
    r = requests.post(url = "http://owenserver.us.to:23654", data = {'content':send})
data = r.text
print(data)
