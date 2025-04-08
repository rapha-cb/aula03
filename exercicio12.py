num = int(input("digite um numero para exibir a tabuada: "))
tabuada = 1
for i in range(1, 11):
    tabuada = num * i
    print(f"{num} X {i} = {tabuada}")