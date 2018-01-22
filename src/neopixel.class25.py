import machine, time, sys
from uos import urandom
from math import *

PIXEL_PIN = machine.Pin(2, machine.Pin.OUT)

#PIXEL_COUNT = 24
PIXEL_COUNT = 64

from neopixel import NeoPixel

class MyNeoPixel(NeoPixel):

    def __init__(self, pixelPin, pixelCount, defaultColor=(80,10,30), defaultStart=(6,6,6), clearPixel=True):
        super().__init__(pixelPin, pixelCount)
        self.rot, self.gruen, self.blau=defaultColor

        self.rotStart=int(self.rot/defaultStart[0])
        self.gruenStart=int(self.gruen/defaultStart[1])
        self.blauStart=int(self.blau/defaultStart[2])
        self.pixelCount=pixelCount
        
        if clearPixel:
           self.fill((0,0,0))
           self.write()

    def setStartFarbe(self,color):
        self.rotStart, self.gruenStart, self.blauStart=color
        
    def getStartFarbe(self):
        return (self.rotStart,self.gruenStart,self.blauStart)
        
    def setFarbe(self,color):
        self.rot, self.gruen, self.blau=color
        
    def getFarbe(self):
        return (self.rot,self.gruen,self.blau)
        
    def getPixelCount(self):
        return (self.pixelCount)
        
    def fillAll(self, color):
        self.fill(color)
        self.write()

    def aufdimmen(self,pixel,Schritte=200):
       for j in range(Schritte):
         for i in pixel:
            self[i]=((self.rotStart+int(self.rot/Schritte*j),self.gruenStart+int(self.gruen/Schritte*j),self.blauStart+int(self.blau/Schritte*j)))
            self.write()
         
    def abdimmen(self,pixel,Schritte=200):
       for j in range(Schritte):
         for i in pixel:
            self[i]=((self.rotStart+int(self.rot-self.rot/Schritte*j),self.gruenStart+int(self.gruen-self.gruen/Schritte*j),self.blauStart+int(self.blau-self.blau/Schritte*j)))
            self.write()

    def schieberechts(self, erstes=0, letztes=-1, schreiben=True):
       if letztes == -1:
          letztes = self.pixelCount-1
       letzte=self[letztes]
       for i in range(letztes,erstes-1,-1):
          if i>0:
             self[i]=self[i-1]
          else:
             self[i]=letzte
       if schreiben:
          self.write()

    def schiebelinks(self, erstes=0, letztes=-1, schreiben=True):
       if letztes == -1:
          letztes=self.pixelCount-1
       letzte=self[erstes]
       for i in range(erstes, letztes+1):
          if i<letztes:
             self[i]=self[i+1]
          else:
             self[i]=letzte
       if schreiben:
          self.write()

    def randrange(self, min_value, max_value):
       # Simple randrange implementation for ESP8266 uos.urandom function.
       # Returns a random integer in the range min to max.  Supports only 32-bit
       magnitude = abs(max_value - min_value)
       randbytes = urandom(4)
       offset = int((randbytes[3] << 24) | (randbytes[2] << 16) | (randbytes[1] << 8) | randbytes[0])
       offset %= (magnitude+1)  # Offset by one to allow max_value to be included.
       return min_value + offset

    def random(self, num, maxHelligkeit = 40):
        self.fill((0,0,0))
        self.write()
        j = self.randrange(1, num)
        for i in range(j):
           x0 = self.randrange(0, PIXEL_COUNT-1)
           r = self.randrange(0, maxHelligkeit)
           g = self.randrange(0, maxHelligkeit)
           b = self.randrange(0, maxHelligkeit)
           self[x0]=((r,g,b))
        self.write()

if __name__ == '__main__':
    
    np = MyNeoPixel(PIXEL_PIN, PIXEL_COUNT)
    time.sleep(1)
    
    for i in range(PIXEL_COUNT):
       np.random(5)
       time.sleep_ms(10)
    
    np.fillAll((0,0,0))
    
    np[0]=((10,40,10))
    np[int(PIXEL_COUNT-1-(PIXEL_COUNT/4))]=((10,0,80))
    np[int(PIXEL_COUNT/4)]=((30,20,80))
    np[PIXEL_COUNT-1]=((80,30,30))
    np.write()
    
    for i in range(PIXEL_COUNT/2-1):
       np.schieberechts(0,31,False)
       np.schiebelinks(32,63,False)
       np.write()
       time.sleep_ms(100)
    for i in range(PIXEL_COUNT/2-1):
       np.schiebelinks(0,31,False)
       np.schieberechts(32,63,False)
       np.write()
       time.sleep_ms(100)
    
    led_startcolor = np.getStartFarbe()
    led_color = np.getFarbe()
    np.fillAll(led_startcolor)
    np.setFarbe((0,0,40))
    np.aufdimmen([0,14,18])
    np.abdimmen([0])
    time.sleep(1)

    np.fillAll((0,0,0))
    np.setFarbe(led_color)
    np.setStartFarbe(led_startcolor)
    for i in range(PIXEL_COUNT-1,-1,-1):
        np.aufdimmen([i])
        np.abdimmen([i])
        time.sleep_ms(50)

