import pyb
from pyb import Pin
from ds18x20 import DS18X20
from pyb import Timer
import micropython

micropython.alloc_emergency_exception_buf(100)
tempValue = 0
print('pin init')
Pin('Y11',Pin.OUT_PP).low() #GND
Pin('Y9',Pin.OUT_PP).high() #VCC

def displayTemp(t):
 print('Current Temperature:')
 print(tempValue)
 
tim1 = Timer(1)
tim1.callback(displayTemp)
tim1.init(freq=1/5)
 
if __name__=='__main__':
 DQ=DS18X20(Pin('Y10')) #DQ
 while True:
  tempValue = DQ.read_temp()
  