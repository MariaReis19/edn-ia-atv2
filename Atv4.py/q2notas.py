"""2 - Criar um código que registre as notas de alunos e calcular a média da turma."""

# Função para registrar notas 
def registrar_notas():
    notas = []
    while True:
        entrada = input("Digite a nota do aluno ou FIM para encerrar: ")
        if entrada.lower() == 'fim':
            break # encerra a entrada de notas
        
        # calcular a média das notas válidas 
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("Nota inválida. Por favor, insira uma nota entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido ou 'fim'.")

    # Calcula e exibe a média das notas válidas 
    if notas:
        media = sum(notas) / len(notas)
        print(f"A média da turma é: {media:.2f}")
    else:
        print("Nenhuma nota válida foi registrada.")
registrar_notas()
