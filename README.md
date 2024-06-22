# FastAPI Translation Service

This project utilizes FastAPI to provide a translation service between Uzbek (uz) and English (en) languages. It integrates with a SQLite database (`dictionary.db`) to store and retrieve translations dynamically.

## Features

- **Translation Endpoints:**
  - `/uz_en/{prefix}`: Translates Uzbek words to English.
  - `/en_uz/{prefix}`: Translates English words to Uzbek.
  - `/translate/{prefix}`: Auto-detects the language of the prefix and provides the corresponding translation.

- **Database Integration:** Utilizes SQLite database (`dictionary.db`) to store translations and avoid redundant translation requests.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   
2. Install dependencies:
    ```bash
   pip install -r requirements.txt

## Usage
1. Run the FastAPI server:
    ```bash
   uvicorn main:app --reload

2. Navigate to http://localhost:8000/docs in your browser to access the interactive API documentation (Swagger UI). Here, you can test each endpoint with sample requests.

## Dependencies
 - fastapi: FastAPI framework for building APIs with Python.
 - uvicorn: ASGI server implementation, used to run FastAPI applications.
 - translate: Library for language translation.
 - uz_en_database: Custom module (helperDB) for SQLite database interaction.

## License
This project is licensed under the MIT License - see the LICENSE file for details.