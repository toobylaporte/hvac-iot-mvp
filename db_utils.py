# db_utils.py
import psycopg2
import os

DB_URI = os.getenv("https://pzpegcslpeosvkouptfy.supabase.co")  # Sur ElephantSQL, ex: "postgres://user:pass@host:port/dbname"

def get_connection():
    return psycopg2.connect(DB_URI, sslmode='require')

def create_table_if_not_exists():
    # On crée une table "sensor_data" si elle n'existe pas
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id SERIAL PRIMARY KEY,
            sensor_id VARCHAR(50),
            value DOUBLE PRECISION,
            timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        );
    """)
    conn.commit()
    cur.close()
    conn.close()

def insert_sensor_data(sensor_id, value):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO sensor_data (sensor_id, value)
        VALUES (%s, %s)
    """, (sensor_id, value))
    conn.commit()
    cur.close()
    conn.close()

def get_recent_data(limit=100):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT sensor_id, value, timestamp
        FROM sensor_data
        ORDER BY timestamp DESC
        LIMIT %s
    """, (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows
