# import library yang di butuhkan
import sys
import RPi.GPIO as GPIO
import os
from time import sleep
import Adafruit_DHT
import urllib2



DEBUG = 1

# Setup pin connect ke GPIO
RCpin = 24  #light sensor di pin 24
DHTpin = 23 #DHT sensor di pin 23

#Setup API thingspeak
myAPI = "API KEYS"
myDelay = 60 #waktu (detik) delay untuk mengirim data

GPIO.setmode(GPIO.BCM)
GPIO.setup(RCpin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)



def getSensorData():
    RHW, TW = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, DHTpin)

    #konversi suhu celcius ke farenheit
    TWF = 9/5*TW+32

    #mengembalikan nilai
    return (str(RHW), str(TW),str(TWF))

def RCtime(RCpin):
    LT = 0

    if (GPIO.input(RCpin) == True):
        LT += 1
    return (str(LT))

# fungsi utama
def main():

    print 'memulai...'

    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print baseURL

    while True:
        try:
            RHW, TW, TWF = getSensorData()
            LT = RCtime(RCpin)
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW)+
                                "&field4=%s" % (LT))
            print f.read()
            print TW + " " + TWF+ " " + RHW + " " + LT
            f.close()


            sleep(int(myDelay))
        except:
            print 'exiting.'
            break

# memanggil fungsi utama main()
if __name__ == '__main__':
    main()
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print baseURL

    while True:
        try:
            RHW, TW, TWF = getSensorData()
            LT = RCtime(RCpin)
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW)+
                                "&field4=%s" % (LT))
            print f.read()
            print TW + " " + TWF+ " " + RHW + " " + LT
            f.close()


            sleep(int(myDelay))
        except:
            print 'exiting.'
            break

# memanggil fungsi main()
if __name__ == '__main__':
    main()

if __name__ == '__main__':
    main()
    baseURL = 'https://api.thingspeak.com/update?api_key=%s' % myAPI
    print baseURL

    while True:
        try:
            RHW, TW, TWF = getSensorData()
            LT = RCtime(RCpin)
            f = urllib2.urlopen(baseURL +
                                "&field1=%s&field2=%s&field3=%s" % (TW, TWF, RHW)+
                                "&field4=%s" % (LT))
            print f.read()
            print TW + " " + TWF+ " " + RHW + " " + LT
            f.close()


            sleep(int(myDelay))
        except:
            print 'exiting.'
            break

# panggil main()
if __name__ == '__main__':
    main()
