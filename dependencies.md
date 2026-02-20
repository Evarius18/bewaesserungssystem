# Benötigte Bibliothek installieren
## Auf dem Raspberry Pi 5:
- ```sudo apt update```
- ```sudo apt install python3-pip```
- ```pip install adafruit-circuitpython-dht```
- ```pip install adafruit-blinka```

# Pumpe über GPIO steuern
Angenommen:
Pumpe hängt an GPIO17
Über Relais oder Transistor (NICHT direkt an Pi anschließen!)
---
Beispiel mit RPi.GPIO:
```pip install RPi.GPIO```

Dann:

import RPi.GPIO as GPIO```

PUMPE_PIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMPE_PIN, GPIO.OUT)

def pumpe_an():
    GPIO.output(PUMPE_PIN, GPIO.HIGH)

def pumpe_aus():
    GPIO.output(PUMPE_PIN, GPIO.LOW)