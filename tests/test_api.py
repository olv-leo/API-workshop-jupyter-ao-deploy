import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_ola_mundo_status_code():
    response = client.get("/")
    assert response.status_code == 200


def test_ola_mundo_json():
    response = client.get("/")
    assert response.json() == {"Olá": "Mundo"}


def test_listar_produtos_status_code():
    response = client.get("/produtos")
    assert response.status_code == 200


def test_buscar_produto_status_code():
    response = client.get("/produtos/1")
    assert response.status_code == 200
