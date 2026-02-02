import time
from time import strftime, localtime
import random # Für Simulationszwecke
# import board
# import adafruit_dht


# Initializiere die angeschlossenen Sensoren und Aktoren, mit dem jeweiligen Board-Pins
dhtDevice = None  # Platzhalter für das DHT-Gerät
pumpeDevice = None  # Platzhalter für das Pumpen-Gerät

# Schwellwerte für die Feuchtigkeitssteuerung
FEUCHTIGKEITS_SCHWELLE_UNTEN = 30.0  # Prozent
FEUCHTIGKEITS_SCHWELLE_OBEN = 70.0  # Prozent

# Andere Konfigurationsparameter
pumpe_aktiv = False # Status der Pumpe zu Beginn
warten = 10.0  # Wartezeit zwischen den Messungen in Sekunden zu Beginn


# Zeitstempelfunktion
def zeitstempel():
    return time.strftime("%H:%M:%S")

# Hauptlogik der Anwendung - dauerhaftes Auslesen der Sensordaten und Steuern der Aktoren
while True:
    try:
        # Auslesen der Sensordaten
        # humidity = dhtDevice.humidity
        print(f"[{zeitstempel()}] Lese Feuchtigkeitswert vom Sensor...")
        
        humidity = random.uniform(20.0, 80.0)
        print(f"[{zeitstempel()}] Aktuelle Feuchtigkeit: {humidity:.1f}%")

        # Steuerlogik
        if humidity < FEUCHTIGKEITS_SCHWELLE_UNTEN and not pumpe_aktiv:
            pumpe_aktiv = True
            print(f"[{zeitstempel()}] Feuchtigkeit zu niedrig → Bewässerung STARTEN 💧")
            warten = 5.0  # Kürzere Wartezeit nach dem Starten der Pumpe (um Bewässerung feiner zu steuern)

        elif humidity > FEUCHTIGKEITS_SCHWELLE_OBEN and pumpe_aktiv:
            pumpe_aktiv = False
            print(f"[{zeitstempel()}] Feuchtigkeit hoch genug → Bewässerung STOPPEN 🚫")
            warten = 10.0  # Längere Wartezeit nach dem Stoppen der Pumpe

        else:
            print(f"[{zeitstempel()}] Keine Änderung am Bewässerungszustand")
            
        print(f"[{zeitstempel()}] Pumpe aktiv: {pumpe_aktiv}")

        
    except RuntimeError as error:
        # Behandeln von Lesefehlern
        print(error.args[0])
        time.sleep(2.0)
        continue
    
    except Exception as error:
        # Allgemeine Ausnahmebehandlung
        # dhtDevice.exit()
        raise error

    time.sleep(warten) # Wartezeit zwischen den Messungen, um Fehler beim auslesen zu vermeiden. Zahl in Klammern = Wartezeit in Sekunden
