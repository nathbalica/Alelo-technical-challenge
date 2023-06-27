from flask import *
import pytest
from app import app


@pytest.fixture
def client():
    
    with app.test_client() as client:
        yield client

def test_integration_endpoint(client):
    # Defina os dados para a integração
    data = {
        'tool1_data': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'tool2_data': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }

    # Faça uma requisição POST para a rota da função de integração
    response = client.post('/integration', json=data)

    # Verifique o código de status da resposta
    assert response.status_code == 200

    # Verifique o conteúdo da resposta
    response_data = response.get_json()
    assert 'success' in response_data
    assert response_data['success'] == 'Integração realizada com sucesso'


def test_integration_endpoint_invalid_data(client):
    # Defina os dados para a integração (dados inválidos)
    data = {
        'tool1_data': {
            'key1': 'value1',
            'key2': 'value2'
        }
    }

    # Faça uma requisição POST para a rota da função de integração
    response = client.post('/integration', json=data)

    # Verifique o código de status da resposta
    assert response.status_code == 400, f"Código de status inesperado: {response.status_code}"

    # Verifique o conteúdo da resposta
    response_data = response.get_json()
    assert 'error' in response_data, "A chave 'error' não está presente na resposta"


def test_integration_endpoint_internal_error(client):

    def integration_function():
        raise Exception("Erro interno do servidor: 400 Bad Request: Failed to decode JSON object: Expecting value: line 2 column 1 (char 1)")
    
    app.integration = integration_function

    response = client.post('/integration', json=None)
    response.headers.add('Content-Type', 'application/json')
    assert response.status_code == 500, f"Código de status inesperado: {response.status_code}"
    
    response_data = response.get_json()
    assert 'error' in response_data, "A chave 'error' não está presente na resposta"


def test_integration_endpoint_tool1_error(client):
    # Defina os dados para a integração
    data = {
        'tool1_data': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'tool2_data': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }

    # Faça uma requisição POST para uma rota inválida
    response = client.post('/invalid-route', json=data)

    # Verifique o código de status da resposta
    assert response.status_code == 404, f"Código de status inesperado: {response.status_code}"


def test_integration_endpoint_tool2_error(client):
    # Defina os dados para a integração
    data = {
        'tool1_data': {
            'key1': 'value1',
            'key2': 'value2'
        },
        'tool2_data': {
            'key3': 'value3',
            'key4': 'value4'
        }
    }
    # Faça uma requisição POST para uma rota inválida
    response = client.post('/invalid-route', json=data)

    # Verifique o código de status da resposta
    assert response.status_code == 404, f"Código de status inesperado: {response.status_code}"

