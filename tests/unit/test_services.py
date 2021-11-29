from app.src.services.cnpj_validation.api_brasil import Api_Brasil
from app.src.services.cnpj_validation.cnpj import CNPJ
from app.src.services.cnpj_validation.receita_ws import Receita_WS


def test_api_brasil_service(test_client):
    Api_Brasil('')


def test_cnpj_service(test_client):
    CNPJ('')


def test_receita_ws_service(test_client):
    Receita_WS('')
