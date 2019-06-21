from requests import get
import time
import requests

def run():
    
    url = "https://maker.ifttt.com/trigger/ip_change_email/with/key/Bf91G_MsjKUzsWqRs5N7n"
    ip = "100.35.205.75"
    data = {'value1' : ip}
    
    while 1==1:
        ipNew = get('http://api.ipify.org').text
        if ip.find(ipNew) == 0:
            print ip
        else:
            ip=ipNew
            data = {'value1':ipNew}
            r = requests.post(url, data)
            print "changed"
        
        time.sleep(30)
if __name__ == "__main__":
    from sys import argv
    run()
