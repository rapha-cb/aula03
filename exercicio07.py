combustivel= input("Qual o tipo de gasolina? G para gasolina e E para etanol: ")
litragem= float(input("agora me informe quantos litros voce abasteceu: "))
g= 5.8
e= 4.9
valor = 0
if combustivel == "G" or combustivel == "g":
    valor = litragem * g
elif combustivel == "E" or combustivel == "e":
        vaolor = litragem * e
else:
    print("tipo de combustível inválido")
print(f"voce irá pagar R${valor:.2f}")