import random


def piramide_vertical(nome):
    '''Captura um nome e imprime uma triangulo vertical
        com os caracteres do nome
        ex.:
        entrada: priramide_vertical(PEDRO)
        saida:
        PEDRO
        PEDR
        PED
        PE
        P
    '''
    numero_caracteres = len(nome)
    lista_range = list(range(numero_caracteres))

    for sub_string in lista_range:
        if sub_string == 0:
            print(nome)

        print(nome[0: -sub_string - 1])


def descubra_a_palavra():
    '''Esta função captura uma lista de palavras num arquivo
        .txt e tranforma numa lista de str, uma delas é
        escolhida aleatoriamente e seus caracteres misturados.
        O jogador deve digitar a palavra na ordem correta, o
        mesmo possui três tentativas antes de ser printado a resposta
        correta.
    '''
    with open('./desafio_02/palavras.txt', mode='r') as string_palavras:
        lista = string_palavras.read().split()

    palavra_aleatoria = random.choice(lista)
    tamanho = len(palavra_aleatoria)
    mistura_palavra = "".join(random.sample(palavra_aleatoria, tamanho))
    print(mistura_palavra)

    tentativas = 0
    acerto = 0

    pergunta_entrada = ''
    while tentativas <= 3 or acerto == 0:
        if tentativas == 3:
            print(f'A palavra correta é: {palavra_aleatoria}')
            break
        else:
            pergunta_entrada = input('Digite a palavra em ordem correta:')
            tentativas += 1

        if pergunta_entrada.upper() == palavra_aleatoria:
            acerto += 1
            print('Acertou!')
            break


descubra_a_palavra()
