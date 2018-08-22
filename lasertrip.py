from gpiozero import LightSensor, Buzzer
from time import sleep

Idr = LightSensor(14)
buzzer = Buzzer(17)

while True:
  sleep(0.1)
  if Idr.value <0.5:
     buzzer.on()
     sleep(0.2)
     buzzer.off()
     sleep(0.2)
     buzzer.on()
  else:
      buzzer.off()
  

    
    
  
          
  
      

