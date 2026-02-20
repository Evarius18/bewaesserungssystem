# Benötigte Bibliothek installieren
## Auf dem Raspberry Pi 5:
```sudo apt update```
```sudo apt install python3-pip```
```pip install adafruit-circuitpython-dht```
```pip install adafruit-blinka```

# Pumpe über GPIO steuern
Angenommen:
Pumpe hängt an GPIO17
Über Relais oder Transistor (NICHT direkt an Pi anschließen!)
---
Beispiel mit RPi.GPIO:
```pip install RPi.GPIO```
