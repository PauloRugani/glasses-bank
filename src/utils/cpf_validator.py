def cpf_is_valid(cpf: str) -> bool:
    import re

    cpf = re.sub(r'\D', '', cpf)

    soma_primeiro =  0   
    for i in range(9):
        soma_primeiro += int(cpf[i]) * (10 - i)
    primeiro_digito = 11 - (soma_primeiro % 11)
    primeiro_digito = 0 if 11 - (soma_primeiro % 11) >= 10 else primeiro_digito
    if primeiro_digito != int(cpf[9]):
        return False

    soma_segundo =  0
    for i in range(10):
        soma_segundo += int(cpf[i]) * (11 - i)
    segundo_digito = 11 - (soma_segundo % 11)
    segundo_digito = 0 if segundo_digito >= 10 else segundo_digito

    if segundo_digito != int(cpf[10]):
        return False
    
    return True