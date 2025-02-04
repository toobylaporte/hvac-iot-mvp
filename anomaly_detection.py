# anomaly_detection.py
import time
from db_utils import get_recent_data

def detect_anomalies(threshold=28):
    rows = get_recent_data(limit=10)  # On lit les 10 dernières valeurs
    anomalies = []
    for r in rows:
        sensor_id, value, timestamp = r
        if value > threshold:
            anomalies.append((sensor_id, value, timestamp))
    return anomalies

def main():
    while True:
        anomalies = detect_anomalies()
        if anomalies:
            print("[ALERTE] Anomalies détectées:", anomalies)
            # Ici, on pourrait appeler une API d'ERP (Odoo) pour créer un ticket
            # Ou envoyer un e-mail / Slack
        time.sleep(5)

if __name__ == "__main__":
    main()
