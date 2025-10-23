nota1 = float(input("Digite sua nota no 1° Bimestre:"))
nota2 = float(input("Digite sua nota no 2° Bimestre:"))
nota3 = float(input("Digite sua nota no 3° Bimestre:"))
nota4 = float(input("Digite sua nota no 4° Bimestre:"))

total = nota1 + nota2 + nota3 + nota4

media = total / 4

print(media)

if media >= 7.0:
    print("Aprovado(a) ✅")
elif media >= 5.0 and media < 7.0:
    print("Recuperação ⚠️")
else:
    print("Reprovado(a) ❌🤣🤣🤣🤣🤣")
