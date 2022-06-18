import RPi.GPIO as GPIO
import time
import BHT as DHT
DHTPin = 11 # define the Pin of DHT 11

def loop():
    dht = DHT.DHT(DHTPin) #create a DHT class object
    sumCnt = 0 # number of reading times
    while (True):
        sumCnt += 1
        chk = dht.readDHT11() # read DHT11 and get a return value.
        # Then determine wheter data read is normalaccording to the return value.
        print("The sumCnt is: %d, \t chk : %d"%(sumCnt,chk))
        
        if (chk is dht.DHTLib_OK): #read DHT11 and get a return value
        #Then determine wheter data read is normalaccording to the return value.
            print("DHT11,OK!")
        elif (chk is dht.DHTLIB_ERROR_CHECKSUM): # Data check has errors
            print("DHTLIB_ERROR_CHECKSUM!!")
        elif (chk is dht.DHTLIB_ERROR_TIMEOUT): #reading DHT times out
            print("DHTLIB_ERROR_TIMEOUT!")
        else:
            print("OTHER ERROR")
        print("HUMIDITY : %.2f, \t Temperature : %.2f\n" %(dht.humidity, dht.temperature))
        time.sleep(3)
        
if __name__ == '__main__':
    print ('starting...')
    try:
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
    exit()
            