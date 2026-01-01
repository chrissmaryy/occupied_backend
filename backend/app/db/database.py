import sqlite3
from seeds import reservation_types

# Pfad zur SQLite DB
db_path = "C:/Users/Chrissi/Projects/occupied/occupied/backend/bathroom.db"

# Pfad zur Schema-Datei
schema_path = "schema.sql"

def create_db_and_execute_schema(db_path, schema_path):
    # Verbindung zur DB herstellen (erstellt die Datei, falls sie nicht existiert)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Schema aus der SQL-Datei einlesen
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()

    # Schema ausführen
    cursor.executescript(schema_sql)

    # Reservation Types einfügen
    for rt in reservation_types:
        cursor.execute(
            "INSERT INTO reservation_types (name, description, priority) VALUES (?, ?, ?)",
            (rt["name"], rt["description"], rt["priority"])
        )

    # Änderungen speichern und Verbindung schließen
    conn.commit()
    conn.close()
    print(f"Database '{db_path}' created and schema executed successfully.")

if __name__ == "__main__":
    create_db_and_execute_schema(db_path, schema_path)
