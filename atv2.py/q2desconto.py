"""2- Calculadora de Desconto
Desenvolva um programa que calcula o desconto em uma loja. Use as seguintes informações:

* Nome do produto: "Camiseta"
* Preço original: R$ 50.00
* Porcentagem de desconto: 20%
O programa deve calcular o valor do desconto e o preço final, exibindo todos os detalhes."""



# Dados
produto = "Camiseta"
preco_inicial = 50.00
percentual_desconto = 20

# Cálculos
valor_desconto = preco_inicial * (percentual_desconto / 100)
preco_final = preco_inicial - valor_desconto

# Resultados
print("Produto:", produto)
print("Preço original: R$", preco_inicial)
print("Desconto:", percentual_desconto)
print("Valor do desconto: R$", valor_desconto)
print("Preço final com desconto: R$", preco_final)