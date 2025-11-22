"""4 - Crie um programa que realize consultas a  em relação ao Real (BRL) usando a API mostre valor atual, máxima, mínima e data/hora da última atualização, caso a moeda não existir ou houver erro na requisição, retorne uma mensagem de erro."""
# Solução:
import requests 
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()  # Verifica se houve erro na requisição
        dados = resposta.json()
        
        chave = f"{moeda}BRL"
        if chave in dados:
            cotacao_info = dados[chave]
            valor_atual = cotacao_info.get('bid', 'N/A')
            valor_maximo = cotacao_info.get('high', 'N/A')
            valor_minimo = cotacao_info.get('low', 'N/A')
            data_hora_atualizacao = cotacao_info.get('create_date', 'N/A')
            
            # Exibe as informações da cotação
            print(f"Cotação de {moeda} em relação ao BRL:")
            print("Valor Atual:", valor_atual)
            print("Valor Máximo:", valor_maximo)
            print("Valor Mínimo:", valor_minimo)
            print("Data/Hora da Última Atualização:", data_hora_atualizacao)
        else:
            print("Moeda não encontrada.")
            
    except requests.exceptions.RequestException as e:
        print("Falha na conexão:", e)   
# Solicita ao usuário a moeda
moeda_digitada = input("Digite a sigla da moeda (ex: USD, EUR, GBP): ").upper()
# Chama a função para consultar a cotação
consultar_cotacao(moeda_digitada)