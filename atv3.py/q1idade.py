"""1- Classificador de Idade

Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

*Criança (0-12 anos),
*Adolescente (13-17 anos),
*Adulto (18-59 anos) ou
*Idoso (60 anos ou mais)."""


idade = int(input("Digite sua idade:"))    
if idade >= 0 and idade <= 12:
    print("Aos olhos da sua mãe, você ainda é um baby.")
elif idade >= 13 and idade <= 17:
    print("Aos olhos da sua mãe, você é um aborrecente") 
elif idade >= 18 and idade <= 59:
    print("Aos olhos da sua mãe, você é um caixa eleterônico.")
else:
    print("Já tem netos?")
