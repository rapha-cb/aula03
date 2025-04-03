combustivel= input("Qual o tipo de gasolina? G para gasolina e E para etanol: ")
litragem= float(input("agora me informe quantos litros voce abasteceu: "))
g= 5.8
e= 4.9
if combustivel == "G":
    litragem = litragem * g
else:
    if combustivel == "E":
        litragem = litragem * e

print(f"voce irá pagar R${litragem:.2f}")