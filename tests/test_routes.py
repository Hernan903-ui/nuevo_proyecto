import pytest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from backend.app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_get_products(client):
    response = client.get('/products')
    assert response.status_code == 200
    assert isinstance(response.get_json(), list)  # Asegurarse de que devuelve una lista