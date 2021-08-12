def maior_numero(a, b):
    """Retorna maior valor entre os dois"""
    if a > b:
        print(a)
        return a
    else:
        print(b)
        return b


def media_aritmetica(lista):
    """Retorna a media aritmética de uma lista de números"""
    total = 0
    for numero in lista:
        total += numero

    print(total)
    return total


def quadrado_de_asteriscos(n):
    """Printa um quadrado de asteristicos com lados com comprimento n"""
    forma_lado = ""
    for linha in range(n):
        forma_lado += "*"

    for coluna in range(n):
        print(forma_lado)


LISTA_NOME_PESSOAS = [
    "José",
    "Deuteronômios",
    "Lucas",
    "Nádia",
    "Fernanda",
    "Cairo",
    "Joana",
]


def retorno_nome_mais_comprido(lista):
    """Retorna o nome mais comprido dentro de uma lista de strings"""
    lista_de_comprimentos = []
    for nome in lista:
        lista_de_comprimentos.append(len(nome))

    maior_comprimento, index_maior_comprimento = 0, 0

    for comprimento in lista_de_comprimentos:
        if comprimento > maior_comprimento:
            maior_comprimento = comprimento

        index_maior_comprimento = lista_de_comprimentos.index(
            maior_comprimento
        )

    print(lista[index_maior_comprimento])
    return lista[index_maior_comprimento]


def orcamento_tintas(largura, comprimento):
    """Calcula um orcamento de certa quantidade de latas de tinta pela área"""
    area_retangular = largura * comprimento
    qtd_latas_de_tinta = round(area_retangular / 54)
    custo_total = qtd_latas_de_tinta * 80

    orcamento = [
        f"qtd de latas: {qtd_latas_de_tinta}",
        f"total: R$ {custo_total},00",
    ]

    print(tuple(orcamento))
    return tuple(orcamento)


def tipo_triangulo(a, b, c):
    """Verifica o tipo de triangulo baseado no comprimento dos lados"""
    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        print("não é triangulo")
        return

    if (a == b and a == c) and b == c:
        print("Triângulo Equilátero: três lados iguais")
        return
    elif (a == b and a != c) or (a == c and a != b) or (c == b and c != a):
        print("Triângulo Isósceles: quaisquer dois lados iguais")
        return
    elif (a != b and a != c) and c != b:
        print("Triângulo Escaleno: três lados diferentes")
        return
