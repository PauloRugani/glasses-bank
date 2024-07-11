from cliente.cadastro.client_model import CadastroCliente

nome = {'nome': input('Digite seu nome: '),
        'cpf': input('Digite seu cpf: '),
        'email': input('Digite seu e-mail: '),
        'celular': input('Digite seu numero de celular: '),
        'idade': int(input('Digite sua idade: ')),
        'data_nascimento': input('Digite sua data de nascimento: ')
        }
Paulo = CadastroCliente(**nome)
print(Paulo)

class Cliente:
    def __init__(self, nome, conta, saldo) -> None:
        pass