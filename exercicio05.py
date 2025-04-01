nota1= float(input("digite a primeira nota: "))
nota2= float(input("digite a segunda nota: "))
nota3= float(input("digite a terceira nota: "))

media = (nota1 + nota2 + nota3)/3

if media >= 7:
    print(f"você foi aprovado, média: {media}")
else:
    if media >=4:
        print(f"você está em recuperação, média: {media}")
    else:
        print(f"você foi reprovado, média: {media}")
