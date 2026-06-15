# Catalog API with FastAPI and SQLite

A simple CRUD API for managing a product catalog, built with FastAPI and SQLite.

## Features

- Get all products
- Get a single product by name
- Create a new product
- Update an existing product
- Delete a product
- Input validation with Pydantic
- Error handling for non-existent products

## Tech Stack

- Python 3.13
- FastAPI
- SQLite (via sqlite3)
- Pydantic

## Installation

1. Clone the repository:

   ```bash
 git clone https://github.com/SajjadEf/catalog-api.git
   cd catalog-api
   
   
   
2. Install dependencies:


   ```bash
 pip install fastapi uvicorn
   

## Usage

Run the server:
```bash
python -m uvicorn main_db:app --reload
```
   
   
Open your browser at http://127.0.0.1:8000/docs to see the interactive Swagger documentation.


| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/items` | Get all products |
| GET | `/items/{name}` | Get a single product |
| POST | `/item/{name}` | Create a new product |
| PUT | `/items/{name}` | Update a product |
| DELETE | `/item/{name}` | Delete a product |

## Author

**Sajjad Ef** – [GitHub Profile](https://github.com/SajjadEf)