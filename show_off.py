from __future__ import print_function
import time
import qwiic_icm20948
import sys
import Adafruit_ADS1x15

print("\nSparkFun 9DoF ICM-20948 Sensor  Example 1\n")
IMU = qwiic_icm20948.QwiicIcm20948()
if IMU.connected == False:
        print("The Qwiic ICM20948 device isn't connected to the system. Please check your connection", \
                file=sys.stderr)

IMU.begin()


adc = Adafruit_ADS1x15.ADS1115()

GAIN = 1

print('Reading ADS1x15 values, press Ctrl-C to quit...')
print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*range(4)))
print('-' * 37)
# Main loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*4
    for i in range(4):
        values[i] = adc.read_adc(i, gain=GAIN) #flex sensors data
    """if IMU.dataReady():
        IMU.getAgmt()
        AGM = [IMU.axRaw, IMU.ayRaw, IMU.azRaw, IMU.gxRaw, IMU.gyRaw, IMU.gzRaw, IMU.mxRaw, IMU.myRaw, IMU.mzRaw] #Accelerometre-gyro-magneto data
        values += AGM"""
    n = 0 
    if values[0]>=900 :
        n += 1
    if values[1]>=900 :
        n += 1    
    if values[2]>=900 :
        n += 1 
    if values[3]>=900 :
        n += 1 
    print('Number is : ' + str(n))                 
    time.sleep(0.1)