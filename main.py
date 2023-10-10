from codes.crifra_cesar import criptografar_cifra_cesar, pedir_mensagem_e_chave
from codes.utils_criptografia import get_metodo_criptografia


metodo: str = get_metodo_criptografia()

if metodo != "":
    match metodo:
        case 'cc':
            valores: dict = pedir_mensagem_e_chave()
            print(criptografar_cifra_cesar(mensagem=valores.get('mensagem'), chave=valores.get('chave')))
        case _:
            print(metodo)
            print("Escolha inválida\n")