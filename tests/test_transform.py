import pandas as pd

from src.transform import (
    handle_missing_values,
    remove_duplicates,
    rating_to_numeric,
    clean_names,
    normalize_gender,
    extract_brand,
    parse_string_to_list,
    clean_perfumers_dataset,
    clean_main_accords_dataset,
    extract_notes_from_description,
    extract_years_from_description
)


def test_handle_missing_values():
    df = pd.DataFrame({
        "Name": ["Perfume A", ""],
        "url": ["url1", "url2"]
    })

    result = handle_missing_values(df)

    assert len(result) == 1
    assert result.iloc[0]["Name"] == "Perfume A"


def test_remove_duplicates():
    df = pd.DataFrame({
        "Name": ["A", "A"],
        "url": ["u1", "u1"]
    })

    result = remove_duplicates(df)

    assert len(result) == 1


def test_rating_to_numeric():
    df = pd.DataFrame({
        "Rating Value": ["4.5", "bad_value"],
        "Rating Count": ["1,234", None]
    })

    df["Rating Count"] = df["Rating Count"].astype(str).str.replace(",", "")

    result = rating_to_numeric(df)

    assert result["Rating Value"].iloc[0] == 4.5
    assert pd.isna(result["Rating Value"].iloc[1])
    assert result["Rating Count"].iloc[0] == 1234
    assert result["Rating Count"].iloc[1] == 0


def test_clean_names():
    df = pd.DataFrame({
        "Name": ["Reflection Man for men", "Guidance for women"]
    })

    result = clean_names(df)

    assert result["Name"].iloc[0].strip() == "Reflection Man"
    assert result["Name"].iloc[1].strip() == "Guidance"


def test_normalize_gender():
    df = pd.DataFrame({
        "Gender": [
            "for women",
            "for men",
            "for women and men"
        ]
    })

    result = normalize_gender(df)

    assert result["Gender"].tolist() == [
        "women",
        "men",
        "unisex"
    ]


def test_extract_brand():
    df = pd.DataFrame({
        "url": [
            "https://www.fragrantica.com/perfume/Amouage/Lyric-Man-4622.html"
        ]
    })

    result = extract_brand(df)

    assert result["Brand"].iloc[0] == "Amouage"


def test_parse_string_to_list():
    value = "['woody', 'amber', 'smoky']"

    result = parse_string_to_list(value)

    assert result == ["woody", "amber", "smoky"]


def test_clean_perfumers_dataset():
    df = pd.DataFrame({
        "Perfumers": ["['Quentin Bisch', 'Dominique Ropion']"]
    })

    result = clean_perfumers_dataset(df)

    assert result["Perfumers"].iloc[0] == [
        "Quentin Bisch",
        "Dominique Ropion"
    ]


def test_clean_main_accords_dataset():
    df = pd.DataFrame({
        "Main Accords": ["['woody', 'amber']"]
    })

    result = clean_main_accords_dataset(df)

    assert result["Main Accords"].iloc[0] == [
        "woody",
        "amber"
    ]


def test_extract_notes_from_description():
    df = pd.DataFrame({
        "Description": [
            "Top notes are Bergamot, Lemon; middle notes are Rose, Jasmine; base notes are Musk, Vanilla."
        ]
    })

    result = extract_notes_from_description(df)

    assert result["Top Notes"].iloc[0] == [
        "Bergamot",
        "Lemon"
    ]

    assert result["Middle Notes"].iloc[0] == [
        "Rose",
        "Jasmine"
    ]

    assert result["Base Notes"].iloc[0] == [
        "Musk",
        "Vanilla"
    ]


def test_extract_years_from_description():
    df = pd.DataFrame({
        "Description": [
            "Reflection Man was launched in 2006."
        ]
    })

    result = extract_years_from_description(df)

    assert result["Launch_year"].iloc[0] == 2006