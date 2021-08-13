import random
import json


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


def adivinhe_o_pokemon():
    '''Esta função lê um arquivo JSON de pokemons e escolhe um aleatoriamente
        Logo, o jogador deve digitar o nome do pokemon, se errar é revelado
        uma letra, se acertar vence!
    '''
    with open('./desafio_02/pokemons.json') as file:
        content = file.read()
        pokemons = json.loads(content)['results']

    lista_nome_pokemon = []
    for pokemon in pokemons:
        lista_nome_pokemon.append(pokemon['name'])

    pokemon_aleatorio = random.choice(lista_nome_pokemon)

    contador, acerto, input_pokemon = 1, 0, ''
    while contador < len(pokemon_aleatorio) or acerto == 0:
        if input_pokemon == pokemon_aleatorio:
            print(f'Acertou! Pokemon: {pokemon_aleatorio}')
            acerto += 1
            break
        else:
            input_pokemon = input('Adivinhe o pokemon: ')
            print(f'{pokemon_aleatorio[:contador]}')
            contador += 1

        if contador - 1 == len(pokemon_aleatorio):
            print(f'Você perdeu! Pokemon: {pokemon_aleatorio}')
            break
