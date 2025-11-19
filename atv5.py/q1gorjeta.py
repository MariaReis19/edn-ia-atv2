"""1 - Crie uma função que calcule a gorjeta a ser deixada em um restaurante, baseada no valor total da conta e na porcentagem de
gorjeta desejada. Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros:
a - valor_conta (float): O valor total da conta
b - porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 10 para 10%)
c - retorna: float: O valor da gorjeta calculada"""

def calcular_gorjeta(valor_conta, porcentagem_gorjeta):
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return round(gorjeta, 2)

# Exemplo de uso:
# valor_conta = 150.0
# porcentagem_gorjeta = 10.0
# gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)
# print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
# Saída: O valor da gorjeta é: R$ 15.00
# Entrada do usuário
valor_conta = float(input("Digite o valor total da conta: R$ "))
porcentagem_gorjeta = float(input("Digite a porcentagem de gorjeta desejada (%): "))

# Cálculo da gorjeta
gorjeta = calcular_gorjeta(valor_conta, porcentagem_gorjeta)    

# Exibe o resultado
print(f"O valor da gorjeta é: R$ {gorjeta:.2f}")
