from fastapi import FastAPI

from firebase_admin import db

from src.config.main import conect_to_database
from src.models.cadastro import CadastroCliente

app = FastAPI()
conect_to_database()

@app.post('/clientes')
def cadastro_cliente(data):
    client_data = dict(CadastroCliente(**data))
    db_client = db.reference('Clientes')
    db_client.child('cliente1').set(client_data)
