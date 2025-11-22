"""2 -   Crie um programa que  acesse a API  para buscar um usuário fictício aleatório. exibindo o nome, e-mail e país desse usuário, caso houver erro na conexão, mostre uma mensagem de falha."""

# Solução: 
import requests
def buscar_usuario():
    url = "https://randomuser.me/api/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        
        usuario = dados['results'][0]
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        print("Nome:", nome)
        print("E-mail:", email)
        print("País:", pais)
        
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)

# Chama a função para buscar o usuário aleatório
buscar_usuario()
