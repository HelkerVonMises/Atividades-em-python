def main():
    soma()


def soma():
    print("Programa de soma\n")
    a = int(input("Digite o primeiro número\n"))
    b = int(input("digite outro número\n"))

    c = a + b

    print("Resultado de", a, "+", b, "é", c)

    print("Deseja realizar outra soma?\n")
    d = int(input("1 para sim e 2 para não\n"))

    if d == 1:
        print("Entendido")
        main()

    if d == 2:
        print("É nóis parça")

    else:
        print("Tá de sacanagem???\n")
        soma()


main()
