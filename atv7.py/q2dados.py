"""2 - Crie um programa que cria um arquivo CSV com nome, idade e cidade de algumas pessoas, que este programa escreva os dados em formato tabular e salva no arquivo escolhido pelo usuário,
caso ocorra um erro ao salvar, mostre uma mensagem de falha. """


import pandas as pd

def criar_arquivo_csv(caminho_arquivo):
    dados = {
        'Nome': ['Ana', 'Bruno', 'Carla', 'Daniel'],
        'Idade': [28, 34, 23, 45],
        'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Curitiba']
    }
    
    df = pd.DataFrame(dados)
    
    try:
        df.to_csv(caminho_arquivo, index=False, sep='\t')
        print(f"Arquivo salvo com sucesso em: {caminho_arquivo}")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")
        
caminho_arquivo = input("Digite o caminho onde deseja salvar o arquivo CSV: ")
criar_arquivo_csv(caminho_arquivo)