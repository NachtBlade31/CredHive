from fastapi.testclient import TestClient
from main import app

def test_get_all_credits():
    with TestClient(app) as client:
        response = client.get("/credits")
        assert response.status_code == 200
        assert response.json() != []

def test_get_credit_by_id():
    with TestClient(app) as client:
        # Assuming there's a credit entry with ID 1 in the database
        response = client.get("/credits/3")
        assert response.status_code == 200
        assert response.json()["id"] == 3

    # Test for a non-existent credit entry
    with TestClient(app) as client:
        response = client.get("/credits/999")
        assert response.status_code == 404
        assert "Credit information not found" in response.text

def test_add_credit_info():
    with TestClient(app) as client:
        # Test adding a new credit information
        data = {
            "id": 1,
            "company_name": "Test 2",
            "address": "Test Address",
            "registration_date": "2023-01-01",
            "number_of_employees": 100,
            "raised_capital": 1000000.0,
            "turnover": 500000.0,
            "net_profit": 200000.0,
            "contact_number": "1234567890",
            "contact_email": "test@test.com",
            "company_website": "http://www.test.com",
            "loan_amount": 500000.0,
            "loan_interest": 0.05,
            "account_status": True,
        }
        response = client.post("/credits", json=data, headers={"Authorization": "Bearer fake-token"})
        assert response.status_code == 200

        # Test adding duplicate credit information
        response_duplicate = client.post("/credits", json=data, headers={"Authorization": "Bearer fake-token"})
        assert response_duplicate.status_code == 400
        assert "Entry with this company name already exists" in response_duplicate.text

        # Add more test cases for other scenarios, such as infake input data.

def test_update_credit_info():
    with TestClient(app) as client:
        # Assuming there's an existing credit entry with ID 1
        data_update = {
            "id":3,
            "company_name": "Updated Company Name",
            "address": "Updated Address",
            "registration_date": "2023-01-02",
            "number_of_employees": 120,
            "raised_capital": 1200000.0,
            "turnover": 600000.0,
            "net_profit": 250000.0,
            "contact_number": "9876543210",
            "contact_email": "updated@test.com",
            "company_website": "http://www.updated.com",
            "loan_amount": 600000.0,
            "loan_interest": 0.06,
            "account_status": False,
        }
        response = client.put("/credits/3", json=data_update, headers={"Authorization": "Bearer fake-token"})
        assert response.status_code == 200
        assert response.json()["company_name"] == "Updated Company Name"
        assert response.json()["address"] == "Updated Address"

        # Test updating non-existent credit information
        response_not_found = client.put("/credits/999", json=data_update, headers={"Authorization": "Bearer fake-token"})
        assert response_not_found.status_code == 404
        assert "Credit information not found" in response_not_found.text

        # Add more test cases for other scenarios, such as partial updates.

def test_delete_credit_info():
    with TestClient(app) as client:
        # Assuming there's an existing credit entry with ID 1
        response = client.delete("/credits/1", headers={"Authorization": "Bearer fake-token"})
        assert response.status_code == 200
        assert response.json()["message"] == "Credit information deleted successfully"

        # Test deleting non-existent credit information
        response_not_found = client.delete("/credits/999", headers={"Authorization": "Bearer fake-token"})
        assert response_not_found.status_code == 404
        assert "Credit information not found" in response_not_found.text

        # Add more test cases for other scenarios, such as infake ID format.
