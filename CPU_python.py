__author__ = 'Derandi Hermanda'

#memasukan library 
import httplib, urllib
import time
sleep = 60 #waktu (detik) untuk sleep dan post ke chanel
key = '0TNRE99H970T0VZT'

# ini untuk meng push data ke thinkspeak channel
def thermometer():
    while True:

        #mengambi data temperatur CPU dalam Derajat (C)
        temp = int(open('/sys/class/thermal/thermal_zone0/temp').read()) / 1e3 # Get Raspberry Pi CPU temp

        #mengirim data ke thingspeak
        params = urllib.urlencode({'field1': temp, 'key':key }) 
        headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
        conn = httplib.HTTPConnection("api.thingspeak.com:80")

        try:
            conn.request("POST", "/update", params, headers)
            response = conn.getresponse()
            print temp
            print response.status, response.reason
            data = response.read()
            conn.close()

        except:
            print "connection failed"
        break
#sleep for desired amount of time
if __name__ == "__main__":
        while True:
                thermometer()
                time.sleep(sleep)
  
