"""2-  Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, ignorando espaços e pontuação). Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”."""

import string
def eh_palindromo(texto):
   
    # Remover espaços e pontuação, e converter para minúsculas
    texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())

    # Verificar se o texto é igual ao seu reverso
    return texto_limpo == texto_limpo[::-1]

# Entrada do usuário
texto = input("Digite uma palavra ou frase: ")

# Verificação de palíndromo
if eh_palindromo(texto):
    print("Sim")
else:
    print("Não")


# Exemplo de uso:
# texto = "Ana" 
# resultado = eh_palindromo(texto)
# print(resultado) 
# Saída: True ou False
