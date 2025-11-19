"""Crie um programa que solicite ao usuário que insira números
inteiros. O programa deve continuar solicitando números até
que o usuário digite 'fim'. Para cada número inserido, o
programa deve informar se é par ou ímpar. Se o usuário
inserir algo que não seja um número inteiro, o programa deve
informar o erro e continuar. No final, o programa deve exibir a
quantidade de números pares e ímpares inseridos."""


# Função para verificar se um número é par ou ímpar
def par_ou_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "ímpar"

# Inicializa contadores para números pares e ímpares
pares = 0
impares = 0
while True:
    entrada = input("Digite um número inteiro ou fim para encerrar: ")
    if entrada.lower() == 'fim':
        break  # encerra a entrada de números

    # Tenta converter a entrada para um número inteiro
    try:
        numero = int(entrada)
        tipo = par_ou_impar(numero)
        print(f"O número {numero} é {tipo}.")

        # Atualiza os contadores
        if tipo == "par":
            pares += 1
        else:
            impares += 1
    except ValueError:
        print("Entrada inválida. Por favor, insira um número inteiro ou fim.")

# Exibe a quantidade de números pares e ímpares inseridos
print(f"Quantidade de números pares inseridos: {pares}")
print(f"Quantidade de números ímpares inseridos: {impares}")
