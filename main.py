import time
from time import strftime, localtime
import random # Für Simulationszwecke
# import board
# import RPi.GPIO as GPIO
# import adafruit_dht


# Initializiere die angeschlossenen Sensoren und Aktoren, mit dem jeweiligen Board-Pins
dhtDevice = None  # Platzhalter für das DHT-Gerät
pumpeDevice = None  # Platzhalter für das Pumpen-Gerät

# Schwellwerte für die Feuchtigkeitssteuerung
FEUCHTIGKEITS_SCHWELLE_UNTEN = 30.0  # Prozent
FEUCHTIGKEITS_SCHWELLE_OBEN = 70.0  # Prozent

# Wasserstandssimulation & Pumpenschutz
WASSERSTAND_MIN = 20.0  # Mindest-Wasserstand in %
wasser_ok = True
pumpensperre = False   # verhindert sofortiges Wiederanlaufen


# Andere Konfigurationsparameter
pumpe_aktiv = False # Status der Pumpe zu Beginn
warten = 10.0  # Wartezeit zwischen den Messungen in Sekunden zu Beginn


# Zeitstempelfunktion
def zeitstempel():
    return time.strftime("%H:%M:%S")

# Simulierte Wasserstandsmessung - später echte Sensor Logik
def wasserstand_messen():
    # Simulierter Wasserstand in % Später ersetzen durch echten Sensorwert
    return random.uniform(0.0, 30.0)


# Hauptlogik der Anwendung - dauerhaftes Auslesen der Sensordaten und Steuern der Aktoren
while True:
    try:
        # Auslesen der Sensordaten
        # humidity = dhtDevice.humidity
        print(f"[{zeitstempel()}] ℹ️ Lese Feuchtigkeitswert vom Sensor...")
        
        humidity = random.uniform(20.0, 80.0)
        print(f"[{zeitstempel()}] ℹ️ Aktuelle Feuchtigkeit: {humidity:.1f}%")

        wasserstand = wasserstand_messen()
        print(f"[{zeitstempel()}] ℹ️ Wasserstand Tank: {wasserstand:.1f}%")

        wasser_ok = wasserstand >= WASSERSTAND_MIN

        if not wasser_ok:
            print(f"[{zeitstempel()}] ⚠️ Tank fast leer – Bewässerung gesperrt!")
            
            if pumpe_aktiv:
                pumpe_aktiv = False
                pumpensperre = True
                print(f"[{zeitstempel()}] ⚠️ Pumpe wurde gestoppt!")


        # Pumpensperre ggf. aufheben
        if pumpensperre and wasserstand > (WASSERSTAND_MIN + 10):
            pumpensperre = False
            print(f"[{zeitstempel()}] ✅ Tank ausreichend → Pumpensperre aufgehoben")

        
        # Steuerlogik
        if humidity < FEUCHTIGKEITS_SCHWELLE_UNTEN and not pumpe_aktiv and wasser_ok and not pumpensperre:
            pumpe_aktiv = True
            print(f"[{zeitstempel()}] ℹ️ Feuchtigkeit zu niedrig → Bewässerung STARTEN 💧")
            warten = 5.0  # Kürzere Wartezeit nach dem Starten der Pumpe (um Bewässerung feiner zu steuern)

        elif humidity > FEUCHTIGKEITS_SCHWELLE_OBEN and pumpe_aktiv:
            pumpe_aktiv = False
            print(f"[{zeitstempel()}] ℹ️ Feuchtigkeit hoch genug → Bewässerung STOPPEN 🚫")
            warten = 10.0  # Längere Wartezeit nach dem Stoppen der Pumpe

        else:
            print(f"[{zeitstempel()}] ✅ Keine Änderung am Bewässerungszustand")
            
        print(f"[{zeitstempel()}] ℹ️ Pumpe aktiv: {pumpe_aktiv}")

        
    except RuntimeError as error:
        # Erwarteter Laufzeit-/Lesefehler → Meldung ausgeben, kurz warten und erneut versuchen
        print(error.args[0])
        time.sleep(2.0)
        continue
    
    except Exception as error:
        # Unerwarteter Fehler → weiterwerfen, damit das Programm abbricht
        # dhtDevice.exit()
        raise error

    time.sleep(warten) # Wartezeit zwischen den Messungen, um Fehler beim auslesen zu vermeiden. Wert in Klammern = Wartezeit in Sekunden -> hier via Variable steuerbar
