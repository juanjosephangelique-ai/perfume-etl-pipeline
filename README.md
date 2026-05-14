# 🧴 Perfume ETL Pipeline

![Python](https://img.shields.io/badge/python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)
![ETL](https://img.shields.io/badge/pipeline-ETL-orange.svg)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-blue.svg)
![Docker](https://img.shields.io/badge/container-Docker-blue.svg)

---

## 📌 Description

Ce projet est un **pipeline ETL (Extract, Transform, Load)** qui traite un dataset de parfums afin de le nettoyer, le structurer et le charger dans une base de données **SQLite relationnelle**.

Il inclut également une automatisation de tests via **CI/CD (GitHub Actions)** ainsi qu’une **containerisation avec Docker** pour garantir la reproductibilité du pipeline.

---

## ⚙️ Fonctionnalités

- 📥 Ingestion de données CSV
- 🧹 Nettoyage et transformation des données (valeurs manquantes, doublons, normalisation)
- 🔄 Modélisation relationnelle (brands, notes, accords, perfumers)
- 🗄️ Chargement dans une base SQLite
- 🧪 Tests unitaires avec Pytest
- ⚙️ CI/CD avec GitHub Actions (tests automatiques)
- 🐳 Containerisation avec Docker

---

## 🏗️ Architecture du projet
