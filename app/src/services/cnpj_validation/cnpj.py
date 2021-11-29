import re
from app.src.services.cnpj_validation.api_brasil import Api_Brasil
from app.src.services.cnpj_validation.receita_ws import Receita_WS

multipliers = [[5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2], [6, 5, 4, 3, 2, 9, 8, 7, 6, 5, 4, 3, 2]]


class CNPJ:
    """Class that formats a CNPJ given any text and returns if its valid or not"""

    def __init__(self, cnpj: str):
        self.cnpj = self.clean_cnpj(cnpj)
        self.is_valid = None
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

    @staticmethod
    def clean_cnpj(cnpj):
        cnpj = cnpj.strip().split(' ')[0]
        remove_chars = ['.', ',', '-', ' ', '/', '\\']
        for char in remove_chars:
            cnpj = cnpj.replace(char, '')
        return cnpj

    def cnpj_is_valid(self):
        digit_1 = 0
        digit_2 = 0
        if not re.fullmatch(re.compile(r'[0-9]{14}'), self.cnpj):
            return False

        for index, mult in enumerate(multipliers[0]):
            digit_1 = digit_1 + (int(self.cnpj[index]) * mult)
        digit_1 = 11 - (digit_1 % 11)
        digit_1 = 0 if digit_1 >= 10 else digit_1

        for index, mult in enumerate(multipliers[1]):
            digit_2 = digit_2 + (int(self.cnpj[index]) * mult)
        digit_2 = 11 - (digit_2 % 11)
        digit_2 = 0 if digit_2 >= 10 else digit_2

        if self.cnpj[-2:] == '{digit_1}{digit_2}'.format(digit_1=digit_1, digit_2=digit_2):
            return True
        return False

    def get_receitaws_info(self):
        receita_ws = Receita_WS(self.cnpj)
        self.is_valid = receita_ws.is_valid
        self.social_reason = receita_ws.social_reason
        self.cnae = receita_ws.cnae
        self.cnae_description = receita_ws.cnae_description
        self.address = receita_ws.address
        self.address_number = receita_ws.address_number
        self.complement = None
        self.neighborhood = receita_ws.neighborhood
        self.zip_code = receita_ws.zip_code
        self.state = receita_ws.state
        self.city = receita_ws.city

    def get_api_brasil_info(self):
        api_brasil = Api_Brasil(self.cnpj)
        self.is_valid = api_brasil.is_valid
        self.social_reason = api_brasil.social_reason
        self.cnae = api_brasil.cnae
        self.cnae_description = api_brasil.cnae_description
        self.address = api_brasil.address
        self.address_number = api_brasil.address_number
        self.complement = None
        self.neighborhood = api_brasil.neighborhood
        self.zip_code = api_brasil.zip_code
        self.state = api_brasil.state
        self.city = api_brasil.city

    def get_cnpj_additional_information(self):
        self.get_api_brasil_info()
        if not self.is_valid:
            self.get_receitaws_info()
