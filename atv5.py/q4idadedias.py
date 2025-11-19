"""4 - Crie um programa que calcule a quantos dias um individuo está vivo de acordo com a data do dia."""


# Calculo de dias vivo:  
from datetime import datetime
def calcular_dias_vivo(data_nasc):
    data_nasc = datetime.strptime(data_nasc, "%d/%m/%Y")
    data_atual = datetime.now()
    dias_vivo = (data_atual - data_nasc).days
    return dias_vivo

# Entrada do usuário
data_nasc = input("Digite sua data de nascimento (dd/mm/aaaa): ")
# Cálculo dos dias vivo
dias_vivo = calcular_dias_vivo(data_nasc)
# Exibe o resultado
print(f"Você está vivo há {dias_vivo} dias.")



# Exemplo de uso:
# data_nascimento = "01/01/2000"
# dias_vivo = calcular_dias_vivo(data_nasc)   
# print(f"Você está vivo há {dias_vivo} dias.")
# Saída: Você está vivo há XXXX dias.
