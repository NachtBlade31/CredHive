# FastAPI Credit Information API

This FastAPI application provides a RESTful API for managing credit information. It includes CRUD operations, data validation, rate limiting, and token-based authentication.

## Requirements

- Python 3.7 or higher
- Pip (Python package installer)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NachtBlade31/CredHive.git
    cd CredHive
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

## Running the Application

1. Run the FastAPI application using Uvicorn:

    ```bash
    uvicorn main:app --reload
    ```


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

## Configuration

Edit the `main.py` file to configure the database URL and other settings if needed.

## API Endpoints

- `GET /credits`: Retrieve a list of all credit information.
- `GET /credits/{id}`: Retrieve credit information for a specific user by ID.
- `POST /credits`: Add new credit information.
- `PUT /credits/{id}`: Update credit information for a specific user.
- `DELETE /credits/{id}`: Delete credit information for a specific user.

# FastAPI Endpoint Testing Tutorial

## Using HTTPie

1. **Install HTTPie:**
   - If you haven't installed HTTPie, you can do so with the following commands:
     ```bash
     # On Linux
     sudo apt-get install httpie

     # On macOS
     brew install httpie

     # On Windows (requires Python)
     pip install httpie
     ```

2. **Run Endpoints with HTTPie:**
   - Open a terminal window.
   - Use HTTPie to send requests to your FastAPI server. For example:
     ```bash
     # Get all credits
     http GET http://127.0.0.1:8000/credits "Authorization:Bearer fake-token"

     # Get credit by ID
     http GET http://127.0.0.1:8000/credits/1 "Authorization:Bearer fake-token"

     # Add new credit
     http POST http://127.0.0.1:8000/credits "Authorization:Bearer fake-token" id=999 company_name="New Company" address="New Address" registration_date="2022-01-01" number_of_employees:=100 raised_capital:=1000000.0 turnover:=500000.0 net_profit:=200000.0 contact_number="1234567890" contact_email="new@example.com" company_website="http://www.newcompany.com" loan_amount:=500000.0 loan_interest:=5.0 account_status:=true

     # Update credit by ID
     http PUT http://127.0.0.1:8000/credits/1 "Authorization:Bearer fake-token" company_name="Updated Company" number_of_employees:=150 raised_capital:=1200000.0

     # Delete credit by ID
     http DELETE http://127.0.0.1:8000/credits/1 "Authorization:Bearer fake-token"
     ```
   - Adjust the URL and payload data based on your needs.

These are basic examples, and you may need to adjust the requests based on the specific data and endpoints you want to test. Always ensure that the server is running and reachable before attempting to send requests.

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
14. ID

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
