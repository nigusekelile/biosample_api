# biosample_api
## Overview

The BioSample Metadata Management & QC API is a backend system designed to help researchers, laboratory personnel, and bioinformaticians store, organize, and validate biological sample metadata. The project provides a structured way to manage sample information—such as organism type, collection details, and sequencing method—while also performing basic quality checks (QC) to ensure metadata completeness and consistency.
Built using Django REST Framework, this API serves as a foundational bioinformatics tool that can be extended with filtering, exporting, authentication, and automated QC workflows. A backend system for managing biological sample metadata and performing QC integrity checks.

## Features
- BioSample creation & metadata storage
- Configurable metadata fields
- QC rules
- QC reports
- Token authentication
- Django REST API

## Run Locally
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver