# Catalog API

A simple CRUD API for managing a product catalog, built with FastAPI and SQLite.

## Features

- Get all products
- Get a single product by name
- Create a new product
- Update a product
- Delete a product
- Input validation with Pydantic

## Tech Stack

- Python 3
- FastAPI
- SQLite
- Pydantic

## Installation

Clone the repository and install dependencies:

`git clone https://github.com/SajjadEf/catalog-api.git`  
`cd catalog-api`  
`pip install fastapi uvicorn`

## Usage

Run the server:

`python -m uvicorn simple_api_with_db:app --reload`

Then open `http://127.0.0.1:8000/docs`

## API Endpoints

- GET `/items` - All products
- GET `/items/{name}` - One product
- POST `/item/{name}` - Create product
- PUT `/items/{name}` - Update product
- DELETE `/item/{name}` - Delete product

## Author

Sajjad Ef - [GitHub](https://github.com/SajjadEf)
