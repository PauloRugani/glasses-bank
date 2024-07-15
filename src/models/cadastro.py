from pydantic import BaseModel, EmailStr, field_validator
from typing import Optional
import re


from datetime import datetime  

from src.utils.cpf_validator import cpf_is_valid


class CadastroCliente(BaseModel):
    name: Optional[str] = None
    cpf: Optional[str] = None
    email: Optional[EmailStr] = None
    password: Optional[str] = None
    phone_num: Optional[str] = None
    age: Optional[int] = None   
    bith_date: Optional[str] = None

    #retira todos os caracteres na numericos, verifica se tem 11 digitos e verifica se é um cpf valido
    @field_validator('cpf', mode='before')
    def cpf_validator(cls, value):
        value = re.sub(r'\D', '', value)
        if len(value) != 11:
            raise ValueError('Verifique se o cpf foi digitado corretamente')
        if not cpf_is_valid(value):
            raise ValueError('CPF não cadastrado no banco nacional de cadastro de pessoa física')
        return value
    
    #deica qualquer numero no formato xxxxxxxxxxxxx ou +xxxxxxxxxxxxx
    @field_validator('phone_num', mode='before')
    def phone_num_validator(cls, value: str):
        value = re.sub(r'[^\d]', '', value)
        if not value.startswith('55'):
            value = '55' + value
        if len(value) != 13:
            raise ValueError('Digite um número válido')
        return value
    

    @field_validator('password', mode='before')
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValueError('Senha deve conter no mínimo 8 caracteres')
        return value
    
    @field_validator('bith_date', mode='before')
    def date_validator(cls, value: str):
        value = re.sub(r'[^\d]', '', value)
        if len(value) != 8:
            raise ValueError('Data inválida')
        value = datetime.strptime(value, '%d%m%Y')
        value = value.strftime('%d/%m/%Y')
        return value
    



