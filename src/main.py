from init_db import initialize_database
from ingest import ingest_data
from transform import clean_data
from load import load_data
import os



def main():
    print("Début du pipeline ETL")

    # 1. Initialisation de la base de données
    print("Initialisation de la base de données...")
    initialize_database("data/processed/perfumes.db")

    # 2. Ingestion
    print("Ingestion des données...")
    os.makedirs("data/processed", exist_ok=True)
    df_raw = ingest_data("data/raw/fra_perfumes.csv")

    if df_raw is None:
        print("Pipeline arrêté : Impossible de charger les données.")
        return
    
    # 3. Transformation
    print("Transformation des données...")
    df_clean = clean_data(df_raw)

    # 4. Load
    print("Chargement en base de données...")
    load_data(df_clean, db_path="data/processed/perfumes.db")

    print("Pipeline terminé avec succès")


if __name__ == "__main__":
    main()