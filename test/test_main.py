from fastapi.testclient import TestClient
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from main import api


client = TestClient(api)


def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Message": "Welcome to the Ticket Booking System"}


def test_create_ticket():
    response = client.post("/ticket", json={
        "id": 1,
        "flight_name": "Air Asia",
        "flight_date": "2025-10-15",
        "flight_time": "14:30",
        "destination": "Singapore"
    })
    assert response.status_code == 200
    assert response.json()["flight_name"] == "Air Asia"


def test_get_tickets():
    response = client.get("/ticket")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


def test_update_ticket():
    response = client.put("/ticket/1", json={
        "id": 1,
        "flight_name": "Air Asia Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:00",
        "destination": "Malaysia"
    })
    assert response.status_code == 200
    assert response.json()["flight_name"] == "Air Asia Updated"


def test_delete_ticket():
    response = client.delete("/ticket/1")
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        "flight_name": "Air Asia Updated",
        "flight_date": "2025-10-16",
        "flight_time": "15:00",
        "destination": "Malaysia"
    }