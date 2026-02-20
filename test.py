import time
import board
import adafruit_dht
import RPi.GPIO as GPIO

# ===== KONFIGURATION =====
FEUCHTE_SCHWELLE = 40      # Prozent
PUMPE_LAUFZEIT = 5         # Sekunden
PUMPE_PIN = 17
WARTEN = 10

# ===== GPIO Setup =====
GPIO.setmode(GPIO.BCM)
GPIO.setup(PUMPE_PIN, GPIO.OUT)

# ===== Sensor =====
dhtDevice = adafruit_dht.DHT22(board.D4)

def zeitstempel():
    return time.strftime("%H:%M:%S")

def pumpe_an():
    GPIO.output(PUMPE_PIN, GPIO.HIGH)

def pumpe_aus():
    GPIO.output(PUMPE_PIN, GPIO.LOW)

while True:
    try:
        temperatur = dhtDevice.temperature
        feuchte = dhtDevice.humidity

        print(f"{zeitstempel()} - Temperatur: {temperatur:.1f}°C  Feuchte: {feuchte:.1f}%")

        if feuchte is not None and feuchte < FEUCHTE_SCHWELLE:
            print(f"{zeitstempel()} - Feuchtigkeit unter Schwelle! Starte Pumpe.")
            pumpe_an()
            time.sleep(PUMPE_LAUFZEIT)
            pumpe_aus()
            print(f"{zeitstempel()} - Pumpe gestoppt.")

        time.sleep(WARTEN)

    except RuntimeError as e:
        print(f"{zeitstempel()} - Messfehler: {e}")
        time.sleep(2)

    except Exception as e:
        GPIO.cleanup()
        dhtDevice.exit()
        raise e