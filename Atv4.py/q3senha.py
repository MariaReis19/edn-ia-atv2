"""3 - Criar um código que serve para verificar se uma senha digitada pelo usuário atende a critérios básicos de segurança.
a - deve ter pelo menos 8 caracteres.
b - deve conter pelo menos um número."""

# Função para verificar se a senha é forte
def senha_forte(senha):
    if len(senha) < 8:
        return False
    if not any(char.isdigit() for char in senha):
        return False
    return True

# Loop para solicitar senhas até que uma forte seja inserida ou o usuário desista
while True:
    senha = input("Digite uma senha ou sair para encerrar: ")
    if senha.lower() == 'sair':
        print("Programa encerrado.")
        break # encerra o programa

    # Verifica se a senha é forte
    if senha_forte(senha):
        print("Senha FORTE registrada com sucesso!")
        break # encerra o loop

    # Senha fraca, solicita nova entrada
    else:
        print("Senha FRACA. Tente novamente.")
