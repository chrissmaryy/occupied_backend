import sqlite3
from seeds import reservation_times
from pathlib import Path

# Pfad zur SQLite DB
DB_PATH = Path(__file__).resolve().parent.parent / "bathroom.db"

# Pfad zur Schema-Datei
schema_path = Path(__file__).resolve().parent / "schema.sql"

def create_db_and_execute_schema(DB_PATH, schema_path):
    # Verbindung zur DB herstellen (erstellt die Datei, falls sie nicht existiert)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    # Schema aus der SQL-Datei einlesen
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()

    # Schema ausführen
    cursor.executescript(schema_sql)

    # Reservation Types einfügen
    for rt in reservation_times:
        cursor.execute(
            "INSERT INTO reservation_times (length_in_minutes) VALUES (?)",
            (rt["length_in_minutes"],)
        )

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    print(f"Database '{DB_PATH}' created and schema executed successfully.")

if __name__ == "__main__":
    create_db_and_execute_schema(DB_PATH, schema_path)
