# Bewässerungssystem

### Links
* https://docs.aws.amazon.com/de_de/iot/latest/developerguide/iot-moisture-raspi-setup.html
* https://www.computerbase.de/forum/threads/raspberrypi-5-dht22-sensor-raumtemperatur-luftfeuchtigkeit-ubuntu.2191608/
* https://www.raspi-config.de/raspberry-pi-sensoren/
* https://www.elektronik-kompendium.de/sites/raspberry-pi/1907101.htm
* https://docs.sunfounder.com/projects/umsk/de/latest/05_raspberry_pi/pi_lesson19_dht11.html
* https://tutorials-raspberrypi.de/bodenfeuchtigkeit-mit-dem-raspberry-pi-messen/
---
* https://youtu.be/fWze-dR5K-I?si=sHnieQwP-aOaqOvI
---
# Hardware (geplant)
---
* https://www.berrybase.de/seeed-grove-wasser-level-sensor-10cm (Wasserstandssensor)
* Wasserpumpe 

---
# Roadmap

## 🌱 Automatisches Bewässerungssystem – Funktionsübersicht
---
### ✅ **Sollte man einbauen (Grundanforderungen)**

*(Pflichtfunktionen / Kernlogik)*

*  Auslesen eines Feuchtigkeitssensors (real oder simuliert)
*  Definition von unteren und oberen Feuchtigkeitsschwellwerten
*  Automatische Aktivierung der Bewässerung bei zu niedriger Feuchtigkeit
*  Automatisches Abschalten der Bewässerung bei ausreichender Feuchtigkeit
*  Hysterese (zwei Schwellwerte, um ständiges Ein-/Ausschalten zu vermeiden)
*  Statusverwaltung der Pumpe (an / aus)
*  Regelmäßige Messintervalle mit Wartezeit
*  Fehlerbehandlung beim Sensorauslesen (z.B. Try/Except)

---

### ⚙️ **Kann man einbauen (Erweiterungen)**

*(Erhöht die Qualität und Stabilität)*

*  Unterschiedliche Messintervalle je nach Pumpenstatus
*  Maximale Laufzeit der Pumpe (Sicherheitsabschaltung)
*  Gleitender Mittelwert mehrerer Messungen
*  Logging der Messwerte (z.B. in Datei)
*  Simulation der Sensorwerte für Testzwecke
*  Klare Trennung von Logik, Sensorik und Aktorik
*  Modularisierung des Codes (Funktionen)

---

### ✨ **Nice to have (Bonus / Kür)**

*(Nicht notwendig, aber sehr gut für Zusatzpunkte)*

*  Zeitabhängige Bewässerung (nur morgens/abends)
*  Tageslimit für Bewässerungen
*  Warnmeldungen bei ungewöhnlichem Verhalten
*  Manueller Override (z.B. per Tastendruck)
*  Anzeige von Trends (Feuchtigkeit steigt/fällt)
*  Web- oder Konsolen-Statusanzeige
*  Vorbereitung für echte Hardware (GPIO / Relais)
*  Umschaltbar zwischen Simulation und Echtbetrieb
