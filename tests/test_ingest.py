import pandas as pd
import os
from src.ingest import load_raw_data


def test_load_raw_data(tmp_path):
    # 1. Créer un CSV temporaire simulant des données brutes
    file_path = tmp_path / "test_data.csv"

    df_input = pd.DataFrame({
        "name": ["Perfume A", "Perfume B"],
        "brand": ["Brand A", "Brand B"],
        "rating": [4.5, 3.8]
    })

    df_input.to_csv(file_path, index=False)

    # 2. Appeler la fonction d'ingestion
    df_output = load_raw_data(str(file_path))

    # 3. Vérifications

    # Le type doit être un DataFrame
    assert isinstance(df_output, pd.DataFrame)

    # Les lignes doivent être correctement chargées
    assert df_output.shape == (2, 3)

    # Les colonnes doivent exister
    assert "name" in df_output.columns
    assert "brand" in df_output.columns
    assert "rating" in df_output.columns

    # Vérification contenu
    assert df_output.iloc[0]["name"] == "Perfume A"