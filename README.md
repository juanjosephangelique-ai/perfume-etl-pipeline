# 🧴 Perfume ETL Pipeline

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![ETL](https://img.shields.io/badge/pipeline-ETL-orange.svg)

## 📌 Description

Ce projet est un **pipeline ETL (Extract, Transform, Load)** qui permet de traiter un dataset de parfums, de le nettoyer, de le normaliser et de le charger dans une base de données **SQLite relationnelle**.

L’objectif est de transformer des données brutes en une structure exploitable pour l’analyse data.

---

## ⚙️ Fonctionnalités

* 📥 Chargement de données CSV (ingestion)
* 🧹 Nettoyage des données (valeurs manquantes, doublons, formats)
* 🔄 Normalisation des entités (brands, notes, accords, perfumers)
* 🗄️ Modélisation relationnelle SQL
* 💾 Chargement dans SQLite
* 🧪 Tests unitaires avec Pytest

---

## 🏗️ Architecture du projet

```
project/
│
├── data/
│   ├── raw/                # Données brutes (CSV)
│   └── processed/          # Données nettoyées (optionnel)
│
├── src/
│   ├── ingest.py          # Chargement des données
│   ├── transform.py       # Nettoyage et transformation
│   ├── load.py            # Chargement en base SQLite
│   └── main.py            # Orchestration du pipeline ETL
│
├── database/
│   └── perfumes.db        # Base SQLite générée
│
├── tests/
│   └── test_transform.py  # Tests unitaires
│
├── requirements.txt
└── README.md
```

---

## 🧱 Schéma de la base de données

### Table `brands`

* id (PK)
* name

### Table `perfumes`

* id (PK)
* name
* brand_id (FK)
* gender
* rating_value
* rating_count
* description
* url

### Table `accords`

* id (PK)
* name

### Table `notes`

* id (PK)
* name

### Table `perfumers`

* id (PK)
* name

### Tables de liaison

* perfume_accords
* perfume_notes
* perfume_perfumers

---

## 🔄 Pipeline ETL

### 1. Extract (Ingestion)

* Lecture du fichier CSV brut
* Chargement en DataFrame Pandas

### 2. Transform

* Suppression des doublons
* Gestion des valeurs manquantes
* Nettoyage des noms
* Conversion des types (ratings, counts)
* Normalisation des entités

### 3. Load

* Création des tables SQLite
* Insertion des données structurées
* Gestion des clés primaires / étrangères

---

## 🚀 Installation

### 1. Cloner le repo

```bash
git clone https://github.com/username/perfume-etl.git
cd perfume-etl
```

### 2. Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## ▶️ Utilisation

### Lancer le pipeline ETL complet

```bash
python src/main.py
```

---

## 🧪 Tests

```bash
pytest tests/
```

---

## 🛠️ Stack technique

* Python 3.10+
* Pandas
* SQLite
* Pytest

---

## 📊 Résultats

Une base de données propre permettant :

* Analyse des marques de parfums
* Étude des accords les plus fréquents
* Analyse des notes et avis utilisateurs
* Exploration des tendances parfum

---

## 🔮 Améliorations futures

* Ajout d’un dashboard (Streamlit / Power BI)
* Orchestration avec Airflow
* CI/CD avec GitHub Actions
* Containerisation avec Docker

---

## 👨‍💻 Auteur

Projet réalisé dans un contexte d’apprentissage Data Engineering / ETL.
