# Bewässerungssystem

---

# Roadmap
## 🌱 Automatisches Bewässerungssystem – Funktionsübersicht

### ✅ **Sollte man einbauen (Grundanforderungen)**

*(Pflichtfunktionen / Kernlogik)*

* — Auslesen eines Feuchtigkeitssensors (real oder simuliert)
* — Definition von unteren und oberen Feuchtigkeitsschwellwerten
* — Automatische Aktivierung der Bewässerung bei zu niedriger Feuchtigkeit
* — Automatisches Abschalten der Bewässerung bei ausreichender Feuchtigkeit
* — Hysterese (zwei Schwellwerte, um ständiges Ein-/Ausschalten zu vermeiden)
* — Statusverwaltung der Pumpe (an / aus)
* — Regelmäßige Messintervalle mit Wartezeit
* — Fehlerbehandlung beim Sensorauslesen (z.B. Try/Except)

---

### ⚙️ **Kann man einbauen (Erweiterungen)**

*(Erhöht die Qualität und Stabilität)*

* — Unterschiedliche Messintervalle je nach Pumpenstatus
* — Maximale Laufzeit der Pumpe (Sicherheitsabschaltung)
* — Gleitender Mittelwert mehrerer Messungen
* — Logging der Messwerte (z.B. in Datei)
* — Simulation der Sensorwerte für Testzwecke
* — Klare Trennung von Logik, Sensorik und Aktorik
* — Modularisierung des Codes (Funktionen)

---

### ✨ **Nice to have (Bonus / Kür)**

*(Nicht notwendig, aber sehr gut für Zusatzpunkte)*

* — Zeitabhängige Bewässerung (nur morgens/abends)
* — Tageslimit für Bewässerungen
* — Warnmeldungen bei ungewöhnlichem Verhalten
* — Manueller Override (z.B. per Tastendruck)
* — Anzeige von Trends (Feuchtigkeit steigt/fällt)
* — Web- oder Konsolen-Statusanzeige
* — Vorbereitung für echte Hardware (GPIO / Relais)
* — Umschaltbar zwischen Simulation und Echtbetrieb
