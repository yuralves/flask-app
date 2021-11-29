import re
import requests


class Receita_WS:
    """Class that verifies a CPNJ in RECEITA FEDERAL endpoints
    Check the documentation here https://receitaws.com.br/api"""

    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.update_receita_info()

    def update_receita_info(self):
        response = requests.get('https://www.receitaws.com.br/v1/cnpj/{cnpj}'.format(cnpj=self.cnpj))
        if response.status_code != 200:
            self.is_valid = False
            self.social_reason = None
            self.cnae = None
            self.cnae_description = None
            self.address = None
            self.address_number = None
            self.complement = None
            self.neighborhood = None
            self.zip_code = None
            self.state = None
            self.city = None
            return
        response = response.json()
        self.is_valid = True
        self.social_reason = response.get('nome')
        self.cnae = None  # response.get('atividade_principal')[0]['code']
        self.cnae_description = None  # response.get('atividade_principal')[0]['text']
        self.address = response.get('logradouro')
        self.address_number = response.get('numero')
        self.complement = None
        self.neighborhood = response.get('bairro')
        self.zip_code = response.get('cep')
        self.state = response.get('uf')
        self.city = response.get('municipio')
