"""1- Conversor de Moeda
Crie um programa que converte um valor em reais para dólares e euros. Use os seguintes dados:

* Valor em reais: R$ 100.00
* Taxa do dólar: R$ 5.20
* Taxa do euro: R$ 6.15
O programa deve calcular e exibir os valores convertidos, arredondando para duas casas decimais."""


# Dados fornecidos
reais = 100.00
dolar = 5.20
euro = 6.15

# Cálculos
valor_dolares = reais / dolar
valor_euros = reais / euro

# Exibição dos resultados com duas casas decimais
print(f"Valor em reais: R$ {reais:.2f}")
print(f"Em dólares: US$ {valor_dolares:.2f}")
print(f"Em euros: € {valor_euros:.2f}")

