import sqlite3, pathlib

# base folder where this script sits
base = pathlib.Path(__file__).resolve().parent
# ensure folder exists
base.mkdir(parents=True, exist_ok=True)

# explicit .db file path as string
db_path = str(base / "dnd.db")
schema_path = base / "schema.sql"

print("DB path:", db_path)
print("Schema exists:", schema_path.exists())

# connect using string
conn = sqlite3.connect(db_path)

# only run schema if it exists
if schema_path.exists():
    with open(schema_path, encoding="utf-8") as f:
        conn.executescript(f.read())
        print("Schema executed.")
else:
    print("schema.sql not found in", schema_path)

conn.commit()
conn.close()
print("Database created successfully.")
