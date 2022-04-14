import time
import hashlib
import ssl
from urllib.request import urlopen, Request

 
# website to monitor


url = Request('https://webserverlb-1229222875.us-east-1.elb.amazonaws.com/',
              headers={'User-Agent': 'Mozilla/5.0'})
            
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE




 
#read website and store it in webcontent
webcontent = urlopen(url, context=ctx).read()
 
#create the initial hash
currentHash = hashlib.sha224(webcontent).hexdigest()

print("running")

time.sleep(10)

while True:
    try:
        #read website and store it in webcontent
        webcontent = urlopen(url, context=ctx).read()
         
        # create a hash
        currentHash = hashlib.sha224(webcontent).hexdigest()
         
        # wait for 30 seconds
        time.sleep(30)
         
        # perform the get request
        webcontent = urlopen(url, context=ctx).read()
         
        # create a new hash
        newHash = hashlib.sha224(webcontent).hexdigest()
 
        # check if new hash is same as the previous hash
        if newHash == currentHash:
            continue
 
        #if new hash doesnt match current hash
        else:
            #alert
            print("something changed")
 
            #read website again
            webcontent = urlopen(url, context=ctx).read()
 
            # create a hash
            currentHash = hashlib.sha224(webcontent).hexdigest()
 
            # wait for 30 seconds
            time.sleep(30)
            continue
             

    except Exception as e:
        print("error")
