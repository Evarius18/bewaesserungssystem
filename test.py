import time
from time import strftime, localtime
# import board
# import adafruit_dht

# Python Datei um Sensorik zu testen (Anschlüsse etc.)

# Initializiere die angeschlossenen Sensoren und Aktoren, mit dem jeweiligen Board-Pins
dhtDevice = None  # Platzhalter für das DHT-Gerät
pumpeDevice = None  # Platzhalter für das Pumpen-Gerät

# Variablen
warten = 10  # Wartezeit zwischen den Messungen in Sekunden

# Zeitstempelfunktion (Debugging)
def zeitstempel():
    return time.strftime("%H:%M:%S")


while True:
    try:
        # Lese die Sensorwerte aus
        feuchte = dhtDevice.feuchte

        # Ausgabe der gelesenen Werte mit Zeitstempel
        print(f"{zeitstempel()} - Temperatur: {temperatur:.1f}°C  Feuchte: {feuchte:.1f}%")

        # Überprüfe, ob die Feuchtigkeit unter dem Schwellenwert liegt
        if feuchte < FEUCHTE_SCHWELLE:
            print(f"{zeitstempel()} - Feuchtigkeit unter Schwelle! Starte Pumpe.")
            pumpeDevice.an()  # Pumpe einschalten
            time.sleep(PUMPE_LAUFZEIT)  # Pumpe für eine bestimmte Zeit laufen lassen
            pumpeDevice.au()  # Pumpe ausschalten
            print(f"{zeitstempel()} - Pumpe gestoppt.")

        # Wartezeit bis zur nächsten Messung
        time.sleep(warten)

    except Exception as e:
        print(f"{zeitstempel()} - Fehler beim Lesen der Sensoren: {e}")
        time.sleep(5)  # Wartezeit bei Fehlern