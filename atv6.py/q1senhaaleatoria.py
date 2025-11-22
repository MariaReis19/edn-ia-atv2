"""1 - Crie um programa que gere senhas aleatórias com letras, números e símbolos e que o usuário  também escolha o tamanho da senha  para criar senhas seguras automaticamente."""

# Solução: 
import random
import string

# Função para gerar senha aleatória
def gerar_senha(tamanho):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    return senha # Retorna a senha gerada

# Solicita ao usuário o tamanho da senha
tamanho_senha = int(input("Digite o tamanho da senha desejada: "))

# Gera a senha
senha_gerada = gerar_senha(tamanho_senha)
# Exibe a senha gerada
print("Senha gerada:", senha_gerada)
