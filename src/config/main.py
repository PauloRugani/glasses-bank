import firebase_admin
from firebase_admin import credentials

#funciona -> faz a conexao com o banco de dados do firebase
def conect_to_database():
    cred = credentials.Certificate('serviceAccountKey.json')  # Substitua com o caminho para o seu arquivo serviceAccountKey.json
    firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://glasses-bank-default-rtdb.firebaseio.com/'
})