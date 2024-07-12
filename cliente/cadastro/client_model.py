from pydantic import BaseModel, EmailStr, field_validator
from dataclasses import dataclass
from typing import Any
import re

import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Passo 1: Inicializar o SDK do Firebase com as credenciais
cred = credentials.Certificate('serviceAccountKey.json')  # Substitua com o caminho para o seu arquivo serviceAccountKey.json
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://glasses-bank-default-rtdb.firebaseio.com/'
})

class CadastroCliente(BaseModel):
    name: str
    cpf: str
    email: EmailStr
    password: str
    phone_num: str
    age: int
    bith_date: str 

    @field_validator('cpf', mode='before')
    def cpf_validator(cls, value):
        if not re.fullmatch(r'\d{3}\.\d{3}\.\d{3}-\d{2}', value):
            if not re.fullmatch(r'\d{11}', value):
                raise ValueError('Verifique se o cpf foi digitado corretamente')
        return value
    
    @field_validator('phone_num', mode='before')
    def phone_num_validator(cls, value: str):
        value = re.sub(r'[()\s-]', '', value)
        return value

    @field_validator('password', mode='before')
    def password_validator(cls, value):
        if len(value) < 8:
            raise ValueError('Senha deve conter no mínimo 8 caracteres')
        return value



# nome = {'name': input('Digite seu nome: '),
#         'cpf': input('Digite seu cpf: '),
#         'email': input('Digite seu e-mail: '),
#         'password': input('Digite uma senha: '),
#         'phone_num': input('Digite seu numero de celular: +55 '),
#         'age': int(input('Digite sua idade: ')),
#         'bith_date': input('Digite sua data de nascimento: ')
#         }
cliente =  db.reference('Clientes')

nome = {'name': 'Paulo',
        'cpf': '04995386505',
        'email': 'phrugany@uol.com.br',
        'password': 'Sousa12.',
        'phone_num': '+5579996380212',
        'age': 19,
        'bith_date': '12/02/2005'
        }

cliente = cliente.child('1')
data = (dict(CadastroCliente(**nome)))

cliente.set(data)