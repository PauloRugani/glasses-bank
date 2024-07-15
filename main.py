from src.routes.main import cadastro_cliente
from src.models.cadastro import CadastroCliente
from src.utils.format_error import DataModel

valid_data = {}
inputs = [('name', 'Digite seu nome'),
        ('cpf', 'Digite seu cpf'),
        ('email', 'Digite seu email'),
        ('password', 'Digite sua senha'),
        ('phone_num', 'Digite seu telefone'),
        ('age', 'Digite sua idade'),
        ('bith_date', 'Digite sua data de nascimento')]

i = 0
key = 0
value = 1
while i < 7:
    try:
        if inputs[i][key] not in valid_data.keys():
            info = input(inputs[i][value])
            check_info = {inputs[i][key] : info}
            data = dict(CadastroCliente(**check_info))
            valid_data.update({inputs[i][key] : data[inputs[i][key]]})
            i += 1
            continue
        break
    except Exception as e:
        print(DataModel.model_data(e))

cadastro_cliente(valid_data)

    