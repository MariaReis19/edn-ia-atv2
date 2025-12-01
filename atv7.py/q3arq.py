"""3 - Crie um programa que leia um arquivo CSV informado pelo usuário, percorrendo cada linha do arquivo e a exibe na tela,
caso o arquivo não seja encontrado, mostre uma mensagem de erro."""

import pandas as pd

def ler_arquivo_csv(caminho_arquivo):
    try:
        df = pd.read_csv(caminho_arquivo)
        
        for index, row in df.iterrows():
            print(row.to_dict())
    
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
        
caminho_arquivo = input("Digite o caminho do arquivo CSV que deseja ler: ")
ler_arquivo_csv(caminho_arquivo)