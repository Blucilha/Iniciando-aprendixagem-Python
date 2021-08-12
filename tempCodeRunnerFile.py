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
        print(" Triângulo Escaleno: três lados diferentes")
        return


tipo_triangulo(1, 1, 2)


tipo_triangulo(4, 1, 4)


tipo_triangulo(1, 1, 1)


tipo_triangulo(4, 5, 3)
