import pandas as pd

def ingest_data(file_path):
    """
    Ingest data from a CSV file and return a DataFrame.

    Parameters:
    file_path (str): The path to the CSV file.

    Returns:
    pd.DataFrame: The ingested data as a DataFrame.
    """

    try:
        df = pd.read_csv(file_path)
        print(f"Data successfully ingested from {file_path}")
        return df
    
    except FileNotFoundError:
        print(f"File not found: {file_path}")

    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")

    except Exception as e:
        print(f"An error occurred while ingesting data: {e}")