"""4 -  Crie um programa que leia e escreva arquivos no formato JSON, que salve em um dicionário com nome, idade e cidade em um arquivo JSON e depois leia o mesmo arquivo exibindo os dados,
caso o arquivo não existir ou ocorrer erro ao salvar, mostre uma mensagem de falha. """


import json

def salvar_dados_json(caminho_arquivo, dados):
    try:
        with open(caminho_arquivo, 'w') as arquivo_json:
            json.dump(dados, arquivo_json, indent=4)
        print(f"Dados salvos com sucesso em: {caminho_arquivo}")
    except Exception as e:
        print(f"Falha ao salvar o arquivo: {e}")

def ler_dados_json(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r') as arquivo_json:
            dados = json.load(arquivo_json)
        print("Dados lidos do arquivo JSON:")
        print(dados)
    except FileNotFoundError:
        print("Erro: O arquivo não foi encontrado.")
    except json.JSONDecodeError:
        print("Erro: O arquivo não contém um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")

caminho_arquivo = input("Digite o caminho do arquivo JSON: ")
dados_para_salvar = { 'Nome': 'Lucas', 'Idade': 30, 'Cidade': 'São Paulo' }
salvar_dados_json(caminho_arquivo, dados_para_salvar)
ler_dados_json(caminho_arquivo)