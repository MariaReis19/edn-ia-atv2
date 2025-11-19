"""1 - Criar um código que faça uma calculadora que tenha as operações básicas(+,-,*,/)."""


def calculadora():
    while True:
        try:
            # Solicita a entrada dos números e a operação ao usuário
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            operacao = input("Digite a operação (+, -, *, /): ")

            # Realiza a operação escolhida pelo usuário e verifica possíveis erros 
            if operacao == '+':
                resultado = num1 + num2
            elif operacao == '-':
                resultado = num1 - num2
            elif operacao == '*':
                resultado = num1 * num2
            elif operacao == '/':
                if num2 == 0:
                    raise ZeroDivisionError("Divisão por zero não é permitida.")
                resultado = num1 / num2
            else:
                raise ValueError("Operação inválida. Use apenas +, -, *, ou /.")
            
            # Exibe resultado e encerra
            print(f"O resultado de {num1} {operacao} {num2} é: {resultado}")
            break # finaliza o programa

        except ValueError as ve:
            print(f"Erro de valor: {ve}. Por favor, tente novamente.")
        except ZeroDivisionError as zde:
            print(f"Erro de divisão: {zde}. Por favor, tente novamente.")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}. Por favor, tente novamente.")
calculadora()




