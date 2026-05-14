import sqlite3
import pandas as pd

def get_or_create_id(cursor, table, name):
    """Récupère l'ID d'une entité ou la crée si elle n'existe pas."""
    if not name or name == "": return None
    
    cursor.execute(f"INSERT OR IGNORE INTO {table} (name) VALUES (?)", (str(name).strip(),))
    cursor.execute(f"SELECT id FROM {table} WHERE name = ?", (str(name).strip(),))
    result = cursor.fetchone()
    return result[0] if result else None

def load_data(df, db_path="../data/processed/perfumes.db"):
    with sqlite3.connect(db_path) as conn:
        conn.execute("PRAGMA foreign_keys = ON;")
        cursor = conn.cursor()

        for _, row in df.iterrows():
            # 1. Gérer la marque
            brand_id = get_or_create_id(cursor, "brands", row['Brand'])

            # 2. Insérer le parfum
            cursor.execute("""
                INSERT OR IGNORE INTO perfumes 
                (name, brand_id, gender, rating_value, rating_count, description, url)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (row['Name'], brand_id, row['Gender'], row['Rating Value'], 
                  row['Rating Count'], row['Description'], row['URL']))
            
            # Récupérer l'ID du parfum (soit le nouveau, soit l'existant via l'URL unique)
            cursor.execute("SELECT id FROM perfumes WHERE url = ?", (row['URL'],))
            perfume_id = cursor.fetchone()[0]

            # 3. Gérer les Parfumeurs (Many-to-Many)
            for p_name in row['Perfumers']:
                p_id = get_or_create_id(cursor, "perfumers", p_name)
                if p_id:
                    cursor.execute("INSERT OR IGNORE INTO perfume_perfumers VALUES (?, ?)", (perfume_id, p_id))

            # 4. Gérer les Accords (Many-to-Many)
            for a_name in row['Main Accords']:
                a_id = get_or_create_id(cursor, "accords", a_name)
                if a_id:
                    cursor.execute("INSERT OR IGNORE INTO perfume_accords VALUES (?, ?)", (perfume_id, a_id))

            # 5. Gérer les Notes (avec le type : top, middle, base)
            note_types = {
                'top': row['Top Notes'],
                'middle': row['Middle Notes'],
                'base': row['Base Notes']
            }
            
            for n_type, notes_list in note_types.items():
                for n_name in notes_list:
                    n_id = get_or_create_id(cursor, "notes", n_name)
                    if n_id:
                        cursor.execute("""
                            INSERT OR IGNORE INTO perfume_notes (perfume_id, note_id, type) 
                            VALUES (?, ?, ?)
                        """, (perfume_id, n_id, n_type))

        conn.commit()
        print("Chargement terminé avec succès !")
