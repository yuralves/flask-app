import requests


class Api_Brasil:
    """Class that verifies a CPNJ in API BRASIL endpoints
    Check the documentation here https://brasilapi.com.br/docs"""

    def __init__(self, cnpj):
        self.cnpj = cnpj
        self.update_api_brasil_info()

    def update_api_brasil_info(self):
        response = requests.get('https://brasilapi.com.br/api/cnpj/v1/{cnpj}'.format(cnpj=self.cnpj))
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
        self.social_reason = response.get('razao_social')
        self.cnae = response.get('cnae_fiscal')
        self.cnae_description = response.get('cnae_fiscal_descricao')
        self.address = response.get('logradouro')
        self.address_number = response.get('numero')
        self.complement = response.get('complemento')
        self.neighborhood = response.get('bairro')
        self.zip_code = response.get('cep')
        self.state = response.get('uf')
        self.city = response.get('municipio')
