# simulate_data.py
import time
import random
from db_utils import insert_sensor_data  # fonction qu'on va définir dans db_utils.py

def simulate_sensor_data(sensor_id, min_val=20, max_val=25):
    """
    Génére des données factices autour de 20-25°C,
    avec parfois un pic pour simuler une anomalie.
    """
    base = random.uniform(min_val, max_val)
    # 5% de chance d’anomalie : +10°C
    if random.random() < 0.05:
        base += random.uniform(5, 10)
    return base

def main():
    sensor_id = "temp1"  # un identifiant de capteur
    while True:
        value = simulate_sensor_data(sensor_id)
        # Insert en base
        insert_sensor_data(sensor_id, value)
        time.sleep(5)  # On publie toutes les 5 secondes

if __name__ == "__main__":
    main()
