import sqlite3

def initialize_database(db_path="../data/processed/perfumes.db"):
    parent_dir = os.path.dirname(db_path)
    if parent_dir:
        os.makedirs(parent_dir, exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("PRAGMA foreign_keys = ON;")

    # Dimension tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS brands (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS accords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS notes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfumers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT UNIQUE NOT NULL
    );
    """)

    # Fact table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfumes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        brand_id INTEGER,
        gender TEXT CHECK(gender IN ('men', 'women', 'unisex')),
        rating_value REAL,
        rating_count INTEGER,
        description TEXT,
        url TEXT UNIQUE,
        FOREIGN KEY (brand_id) REFERENCES brands (id)
    );
    """)

    # Association tables
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfume_accords (
        perfume_id INTEGER,
        accord_id INTEGER,
        PRIMARY KEY (perfume_id, accord_id),
        FOREIGN KEY (perfume_id) REFERENCES perfumes (id) ON DELETE CASCADE,
        FOREIGN KEY (accord_id) REFERENCES accords (id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfume_notes (
        perfume_id INTEGER,
        note_id INTEGER,
        type TEXT CHECK(type IN ('top', 'middle', 'base')),
        PRIMARY KEY (perfume_id, note_id, type),
        FOREIGN KEY (perfume_id) REFERENCES perfumes (id) ON DELETE CASCADE,
        FOREIGN KEY (note_id) REFERENCES notes (id) ON DELETE CASCADE
    );
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS perfume_perfumers (
        perfume_id INTEGER,
        perfumer_id INTEGER,
        PRIMARY KEY (perfume_id, perfumer_id),
        FOREIGN KEY (perfume_id) REFERENCES perfumes (id) ON DELETE CASCADE,
        FOREIGN KEY (perfumer_id) REFERENCES perfumers (id) ON DELETE CASCADE
    );
    """)

    conn.commit()
    conn.close()
    print(f"Base de données initialisée avec succès : {db_path}")