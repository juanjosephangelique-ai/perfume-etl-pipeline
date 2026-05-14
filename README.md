# 🧴 Perfume ETL Pipeline

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![ETL](https://img.shields.io/badge/pipeline-ETL-orange.svg)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue.svg)
![Docker](https://img.shields.io/badge/container-Docker-blue.svg)

---

## 📌 Description

Ce projet est un pipeline ETL (Extract, Transform, Load) qui traite un dataset de parfums afin de le nettoyer, le structurer et le charger dans une base de données SQLite relationnelle.

Il inclut également une automatisation de tests via CI/CD (GitHub Actions) ainsi qu’une containerisation avec Docker pour garantir la reproductibilité du pipeline.

---

## ⚙️ Fonctionnalités

- 📥 Ingestion de données CSV
- 🧹 Nettoyage et transformation des données
- 🔄 Modélisation relationnelle (brands, notes, accords, perfumers)
- 🗄️ Chargement dans SQLite
- 🧪 Tests unitaires avec Pytest
- ⚙️ CI/CD avec GitHub Actions
- 🐳 Dockerisation du projet

---

## 🏗️ Architecture du projet

project/

├── data/
│   ├── raw/
│   └── processed/
│
├── src/
│   ├── ingest.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── database/
│   └── perfumes.db
│
├── tests/
│   ├── test_ingest.py
│   └── test_transform.py
│
├── .github/workflows/
│   └── ci.yml
│
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md

---

## 🧱 Schéma de la base de données

brands:
- id (PK)
- name

perfumes:
- id (PK)
- name
- brand_id (FK)
- gender
- rating_value
- rating_count
- description
- url

accords / notes / perfumers:
Tables normalisées avec relations many-to-many

---

## 🔄 Pipeline ETL

Extract:
- Lecture CSV

Transform:
- Nettoyage
- Suppression doublons
- Normalisation

Load:
- SQLite
- Tables relationnelles

---

## ⚙️ CI/CD (GitHub Actions)

- install dependencies
- run tests (pytest)
- ETL smoke test

---

## 🐳 Docker

Build:
docker build -t perfume-etl .

Run:
docker run --rm perfume-etl

---

## 🚀 Installation

git clone https://github.com/username/perfume-etl.git
cd perfume-etl
pip install -r requirements.txt

---

## ▶️ Usage

python src/main.py

---

## 🧪 Tests

pytest tests/

---

## 🛠️ Stack

Python, Pandas, SQLite, Pytest, GitHub Actions, Docker

---

## 📊 Results

Clean structured perfume database ready for analysis

---

## 🔮 Improvements

- Streamlit dashboard
- Airflow orchestration
- Cloud deployment
- Docker registry

---

## 👨‍💻 Author

Data Engineering ETL project
