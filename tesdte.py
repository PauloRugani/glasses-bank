import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

# Passo 1: Inicializar o SDK do Firebase com as credenciais
cred = credentials.Certificate('serviceAccountKey.json')  # Substitua com o caminho para o seu arquivo serviceAccountKey.json
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://glasses-bank-default-rtdb.firebaseio.com/'
})

# Passo 2: Referência para o banco de dados
ref = db.reference('teste')  # 'teste' é o nome do nó no Realtime Database
ref2 = db.reference('mano')  # 'teste' é o nome do nó no Realtime Database

# Passo 3: Inserir dados
dados = {
    'nome': 'eu',
    'idade': 19,
    'email': 'eu@eu.eu'
}

# uso o set quando eu quero inserir diretamente no no
# ref.set(dados)
# uso o push quando eu quero inserir em outro no com uma chave primaria aleatoria
# ref2.push(dados)

#criar um no dentro de outro
ref.set(dados)

# Passo 4: Recuperar dados
dados_recuperados = ref.parent.get()
print('Dados recuperados:', dados_recuperados)

# Passo 5: Recuperar um dado específico
for key, value in dados_recuperados.items():
    print(value)
    if value.get('nome') == 'Maria':
        print('Dados de Maria:', key, value)
        break
