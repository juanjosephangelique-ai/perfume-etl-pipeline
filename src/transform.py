import pandas as pd
import numpy as np
import re
import ast

def handle_missing_values(df):
    # 1. Replace empty strings or brackets with NaN
    df = df.replace(r'^\s*$|^\[\]$', np.nan, regex=True)

    # 2. Drop rows where all columns except 'url' are NaN
    cols_to_check = [col for col in df.columns if col != 'url']
    df = df.dropna(subset=cols_to_check, how='all')

    print("Missing values handled.")
    return df

def remove_duplicates(df):
    df = df.drop_duplicates()
    print("Duplicates removed.")
    return df

def rating_to_numeric(df):
    df["Rating Value"] = pd.to_numeric(df["Rating Value"], errors="coerce")
    df["Rating Count"] = pd.to_numeric(df["Rating Count"], errors="coerce")
    df["Rating Count"] = df["Rating Count"].fillna(0).astype(int)
    print("Ratings converted to numeric.")
    return df

def clean_names(df):
    df["Name"] = df["Name"].str.strip()

    #Replace "for women", "for men", and "for women and men" from the name of the perfume
    df["Name"] = df["Name"].str.replace("for women and men", "").str.replace("for women", "").str.replace("for men", "")

    print("Names cleaned.")
    return df

def normalize_gender(df):
    df["Gender"] = df["Gender"].replace({
    "for women and men": "unisex",
    "for women": "women",
    "for men": "men"
    })
    return df

def extract_brand(df):
    df["Brand"] = (
        df["url"]
        .str.extract(r"fragrantica\.com/perfume/([^/]+)/")[0]
        .str.replace("-", " ")
        .str.strip()
    )

    print("Brands extracted.")
    return df

def extract_olfactory_notes(description):
    if pd.isna(description) or not isinstance(description, str):
        return {'top': None, 'middle': None, 'base': None}
    
    pattern = r"Top notes are (?P<top>.*?); middle notes are (?P<middle>.*?); base notes are (?P<base>.*)\."
    
    match = re.search(pattern, description)
    
    if match:
        return {
            'top': match.group('top'),
            'middle': match.group('middle'),
            'base': match.group('base')
        }
    return {'top': None, 'middle': None, 'base': None}

def clean_olfactory_notes(note_string):
    if not note_string: return []
    standardized = note_string.replace(' and ', ', ')
    return [n.strip() for n in standardized.split(',')]

def extract_notes_from_description(df):
    notes = df["Description"].apply(extract_olfactory_notes)
    df["Top Notes"] = notes.apply(lambda x: x["top"])
    df["Middle Notes"] = notes.apply(lambda x: x["middle"])
    df["Base Notes"] = notes.apply(lambda x: x["base"])

    df['Top Notes'] = df['Top Notes'].apply(clean_olfactory_notes)
    df['Middle Notes'] = df['Middle Notes'].apply(clean_olfactory_notes)
    df['Base Notes'] = df['Base Notes'].apply(clean_olfactory_notes)
    return df

def parse_string_to_list(value):
    if pd.isna(value):
        return []
    
    if isinstance(value, list):
        return [str(a).strip() for a in value if a is not None]
    
    if isinstance(value, str):
        val = value.strip()
        if val.startswith('[') and val.endswith(']'):
            try:
                parsed = ast.literal_eval(val)
                if isinstance(parsed, list):
                    return [str(a).strip() for a in parsed if a is not None]
            except (ValueError, SyntaxError):
                pass
        
        val = val.replace(' and ', ', ')
        return [item.strip() for item in val.split(',') if item.strip()]
    
    return []

def clean_perfumers_dataset(df):
    df["Perfumers"] = df["Perfumers"].apply(parse_string_to_list)
    return df

def clean_main_accords_dataset(df):
    df["Main Accords"] = df["Main Accords"].apply(parse_string_to_list)
    return df

def extract_years_from_description(df):
    pattern = r"was launched in (\d{4})"

    df["Launch_year"] = (
        df["Description"]
        .str.extract(pattern)[0]
        .astype("Int64")
    )

    return df

def clean_data(df):
    # Handle missing values and remove duplicates
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    # Text cleaning and normalization
    df = rating_to_numeric(df)
    df = clean_names(df)
    df = normalize_gender(df)
    df = clean_main_accords_dataset(df)
    df = clean_perfumers_dataset(df)

    # Feature extraction
    df = extract_notes_from_description(df)
    df = extract_years_from_description(df)
    df = extract_brand(df)

    
    df = df.rename(columns={
        'url': 'URL',
        'rating_value': 'Rating_value',
        'rating_count': 'Rating_count'
    })
    
    print("Data cleaning completed.")
    return df