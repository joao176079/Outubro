import os 
os.system (" cls || clear ")



def calcular_media (nota1 , nota2):
    valor = nota1 + nota2
    if valor <= 200 : 
        print ("Seu valor é muito baixo")
    else : 
        print ("Seu valor é alto ! ")
    return valor



nota1 = int (input ("Digite o seu valor 1 : "))
nota2 = int (input ("Digite o seu valor 2 : "))


resultado = calcular_media (nota1 , nota2)

print (resultado)

