def main():
    print("Programa calculadora")
    choice()


def choice():
    print("\nO que deseja fazer?")
    c = int(input("\n 1 - Soma\n 2 - Subtração\n 3 - Divisão\n "
                  "4 - Multiplicação\n 5 - Radiciação\n 6 - Potência\n 7 - Sair\n"))

    match c:
        case 1:
            soma()
        case 2:
            menos()
        case 3:
            div()
        case 4:
            multi()
        case 5:
            rad()
        case 6:
            poten()
        case 7:
            fim()

    if c != 7:
        outro()


def soma():
    print("Soma\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    mais = a + b
    print("\nResultado =", mais)


def menos():
    print("Subtração\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    sub = a - b
    print("\nResultado =", sub)


def div():
    print("Divisão\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    divi = a / b
    print("\nResultado =", divi)


def multi():
    print("Multiplicação\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    mult = a * b
    print("\nResultado =", mult)


def rad():
    print("Radiciação\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    d = 1 / b
    raiz = a ** d
    print("\nResultado =", raiz)


def poten():
    print("Potenciação\n")
    a = int(input("Digite o primeiro valor\n"))
    b = int(input("Digite o segundo valor\n"))
    pot = a ** b
    print("\nResultado =", pot)


def outro():
    print("\nDeseja fazer mais uma operação?")
    cond = int(input("\n 1 - Sim\n 2 - Não\n"))
    if cond == 1:
        choice()
    else:
        fim()


def fim():
    print("\nObrigado!")


main()
