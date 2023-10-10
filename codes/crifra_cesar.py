from typing import List
from codes.utils_criptografia import alfabeto

def pedir_mensagem_e_chave()-> dict:
    mensagem: str = input("Digite uma mensagem: ")
    chave: int = int(input("Digite um número: "))
    
    return {
        'mensagem': mensagem,
        'chave': chave
    }

def criptografar_cifra_cesar(mensagem: str, chave: int)-> str:
    """Função responsável por criptografar uma mensagem usando Cifra de Cesar

    Args:
        mensagem (str): mensagem que vai ser criptografada
        chave (int): quantas casas o ponteiro vai se mover para mudar as letras

    Returns:
        str: mensagem criptografada
    """
    mensagemSeparada: List[str] = list(mensagem)

    mensagemCripto: str = ""

    for letra in mensagemSeparada:
        for i in range(0, len(alfabeto)):
            if letra.upper() == alfabeto[i].upper():
                novo_indice = (i + chave) % len(alfabeto)
                mensagemCripto += alfabeto[novo_indice]
    return mensagemCripto
