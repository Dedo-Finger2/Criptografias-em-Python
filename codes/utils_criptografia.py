from typing import List

alfabeto: List[str] = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

tecnicas: List[str] = ['cc', 'dd']

"""
    TODO: Concertar o erro aqui: método retorna None caso o primeiro valor a ser inserido seja inválido e o próximo seja válido
"""
def get_metodo_criptografia()-> str:
    metodo: str = input("Qual técnica de criptografia você escolhe? \t[cc] Cifra de Cesar\n")
    
    if metodo in tecnicas:
        return metodo
    else:
        get_metodo_criptografia()