import os
from dataclasses import dataclass
os.system("cls || clear")

#Estrutura de dados.
@dataclass
class Aluno:
    nome:str
    idade:int

#Constante e lista.
QUANTIDADE_ALUNOS=2
lista_alunos=[]

#Solicitando.
print("\n===Solicitando dados aos alunos ===")
for i in range(QUANTIDADE_ALUNOS):
    aluno= Aluno(
        nome=input("Digite seu nome:"),
        idade=int(input("Digite sua idade:"))
    )
    lista_alunos.append(aluno)

#Exbindo
print("\n===Exibindo dados dos alunos ===")
for aluno in lista_alunos:
    print(f"Nome:{aluno.nome}")
    print(f"Idade:{aluno.idade}")

#definindo arquivo para salvar os dados.
nome_do_arquivo="Lista_de_alunos_Senai.txt"
#abrindo arquivo e definindo que será feita a escrita de dados.
with open(nome_do_arquivo, "w") as arquivos_alunos:
    
#Percorrendo o vetor e escrevendo no arquivo uma linha de cada v
    for aluno in lista_alunos:
        arquivos_alunos.write(f"{aluno.nome}, {aluno.idade}\n")

print("\n===Dados dos alunos salvo com sucesso!===")

""""
O conteúdo deste e-mail é de responsabilidade exclusiva do usuário, não cabendo ao SENAI qualquer responsabilidade sobre as
informações divulgadas ou certificação de sua veracidade.
"""