"""3 - Crie um programa que consulte informações de um  na API , retorne logradouro, bairro, cidade e estado do CEP digitado, caso o CEP não existir ou houver erro na requisição, mostre uma mensagem de falha."""


# Solução:
import requests
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        
        # Verifica se o CEP existe
        if 'erro' in dados:
            print("CEP não encontrado.")
        else:
            logradouro = dados.get('logradouro', 'N/A')
            bairro = dados.get('bairro', 'N/A')
            cidade = dados.get('localidade', 'N/A')
            estado = dados.get('uf', 'N/A')
            
            # Exibe as informações do CEP
            print("Logradouro:", logradouro)
            print("Bairro:", bairro)
            print("Cidade:", cidade)
            print("Estado:", estado)
            
            # Exibe as informações do CEP
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)

# Solicita ao usuário o CEP
cep_digitado = input("Digite o CEP (somente números): ")

# Chama a função para consultar o CEP
consultar_cep(cep_digitado)
