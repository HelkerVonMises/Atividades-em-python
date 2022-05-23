print("\t\tPrograma de média\n")
print("Digite as notas e verifique se o aluno está aprovado ou reprovado\n")

a = int(input("Digite a nota 1:\n"))
b = int(input("Digite a nota 2\n"))

c = (a + b) / 2

print("\nMédia =", c)

if c >= 60:
    print("\nAprovado")
else:
    if 60 > c >= 40:
        print("\nRecuperação")
    else:
        if c < 40:
            print("\nReprovado")
