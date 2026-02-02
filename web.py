from flask import Flask, jsonify
import bewaesserung # importiert die Hauptlogik der Bewässerung
main = bewaesserung.Main()

app = Flask(__name__)

@app.route("/")
def index():
    return """
    <h1>🌱 Bewässerungssystem</h1>
    <ul>
        <li>Feuchtigkeit: {:.1f}%</li>
        <li>Pumpe aktiv: {}</li>
    </ul>
    <p>Seite neu laden für aktuelle Werte</p>
    """.format(main.humidity, main.pumpe_aktiv)

@app.route("/api/status")
def status():
    return jsonify({
        "humidity": main.humidity,
        "pumpe_aktiv": main.pumpe_aktiv
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)