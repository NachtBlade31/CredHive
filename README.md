# FastAPI Credit Information API

This FastAPI application provides a RESTful API for managing credit information. It includes CRUD operations, data validation, rate limiting, and token-based authentication.

## Requirements

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:

    - On Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - On macOS/Linux:

        ```bash
        source venv/bin/activate
        ```

4. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

1. Open a Python shell and run the following commands to create the SQLite database tables:

    ```python
    from sqlalchemy import create_engine, MetaData
    from your_app import Base, DATABASE_URL

    engine = create_engine(DATABASE_URL)
    metadata = MetaData()

    Base.metadata.create_all(bind=engine)
    ```

Replace `your_app` with the actual name of your FastAPI application file.

## Running the Application

1. Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```


2. Open your web browser and navigate to `http://127.0.0.1:8000/docs` to access the Swagger UI for testing the API endpoints.

## API Endpoints

- **GET /credits**: Retrieve a list of all credit information.
- **GET /credits/{id}**: Retrieve credit information for a specific user by ID.
- **POST /credits**: Add new credit information.
- **PUT /credits/{id}**: Update credit information for a specific user.
- **DELETE /credits/{id}**: Delete credit information for a specific user.

## Authentication

- Basic token-based authentication is implemented. Use the provided "fake-token" for testing.

## Rate Limiting

- Rate limiting is applied to protect against abuse. The default rate limit is 100 requests per minute.

# FastAPI Credit Information API

## Overview

This FastAPI project provides a RESTful API for managing credit information. The API supports operations such as retrieving a list of all credit information, retrieving information for a specific user by ID, adding new credit information, updating credit information, and deleting credit information.

## Requirements

- Python
- FastAPI framework
- Uvicorn as the ASGI server
- Pydantic for data validation
- SQLite database
- FastAPI Limiter for rate limiting
- Token-based authentication for securing endpoints

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/fastapi-credit-api.git
    cd fastapi-credit-api
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

## Database Setup

This project uses SQLite as the database. The database file will be created automatically when you run the application.

## Configuration

Edit the `main.py` file to configure the database URL and other settings if needed.

## API Endpoints

- `GET /credits`: Retrieve a list of all credit information.
- `GET /credits/{id}`: Retrieve credit information for a specific user by ID.
- `POST /credits`: Add new credit information.
- `PUT /credits/{id}`: Update credit information for a specific user.
- `DELETE /credits/{id}`: Delete credit information for a specific user.

## Data Model

The credit information includes the following fields:

1. Company Name
2. Address
3. Registration Date
4. Number of Employees
5. Raised Capital
6. Turnover
7. Net Profit
8. Contact Number
9. Contact Email
10. Company Website
11. Loan Amount
12. Loan Interest (%)
13. Account Status

## Data Validation

Pydantic models are used for data validation during POST and PUT requests. Ensure that the request data adheres to the defined data model.

## Authentication

Token-based authentication is implemented to secure the API endpoints. Include the authentication token in the request headers.

## Rate Limiting

API security measures include rate limiting using FastAPI Limiter. Requests are limited to prevent abuse.

## How to Run

Use Uvicorn to run the FastAPI application:

```bash
uvicorn main:app --reload
