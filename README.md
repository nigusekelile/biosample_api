# biosample_api

## Overview
`biosample_api` is a Django REST API designed for managing BioSample metadata and performing automated quality control (QC) checks. The BioSample Metadata Management & QC API is a backend system designed to help researchers, laboratory personnel, and bioinformaticians store, organize, and validate biological sample metadata. The project provides a structured way to manage sample information—such as organism type, collection details, and sequencing method—while also performing basic quality checks (QC) to ensure metadata completeness and consistency.
Built using Django REST Framework, this API serves as a foundational bioinformatics tool that can be extended with filtering, exporting, authentication, and automated QC workflows. A backend system for managing biological sample metadata and performing QC integrity checks.
The project supports structured metadata storage, validation, and QC reporting, making it suitable for genomics and bioinformatics workflows.

---

## Features
- BioSample registration and management
- Flexible metadata fields and values
- Quality control (QC) rules and reports
- Token-based authentication
- Modular, scalable backend architecture

---

## Tech Stack
- Python
- Django
- Django REST Framework
- SQLite (development)

---

## Project Structure
- `samples` – BioSample and metadata management
- `qc` – Quality control checks and reports
- `users` – Authentication
- `biosample_api` – Project configuration

---

## Installation

```bash
git clone https://github.com/your-username/biosample_api.git
cd biosample_api
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver

## Run Locally
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
