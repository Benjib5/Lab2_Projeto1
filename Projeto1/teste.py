import random

def cumprimento(texto):
    return f"Olá, {texto}"

def media_aleatoria():
    numeros = [random.randint(1, 100) for _ in range(3)]
    media = sum(numeros) / len(numeros)
    return numeros, media

nome_aluno = "Pedro 'Benji' Bezerra"
mensagem = cumprimento(nome_aluno)
print(mensagem)

numeros, media = media_aleatoria()
print(f"Números sorteados: {numeros}")
print(f"Média: {media:.2f}")
