import os 
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Cliente :
    nome : str
    sobrenome : str
    idade : int
    peso : float
    altura : float

QUANTIDADE_DE_CLIENTES = 4 
lista_de_clientes = []

for i in range (QUANTIDADE_DE_CLIENTES):
    cliente = Cliente(

    
    nome = input ("Digite o seu nome : ")
    sobrenome = (input ("Digite o seu sobrenome : "))
    idade = input ("Digite a sua idade : ")
    peso = input ("Digite o seu peso : ")
    altura = input ("Digite a sua altura : ")
    )
    lista_de_clientes.append(Cliente)


for clientes in lista_de_clientes:
    print(f"Nome:{cliente.nome}")
    print(f"Sobrenome:{cliente.sobrenome}")
    print(f"idade:{cliente.idade}")
    print(f"Peso:{cliente.peso}")
    print(f"Altura:{cliente.altura}")

print("\n===Exibindo dados dos alunos ===")

nome_do_arquivo = "Lista_de_alunos_atividade_txt"
with open (nome_do_arquivo , "w") as arquivos_clientes:

    for clientes in lista_de_clientes:
        arquivos_clientes.write(f"{cliente.nome}, {cliente.sobrenome} , {cliente.idade} , {cliente.peso} , {cliente.altura}")
        