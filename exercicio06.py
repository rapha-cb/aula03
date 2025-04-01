time1= input("diga o nome do primeiro time: ")
gols_time1= int(input("diga quantos gols o primeiro time fez: "))
time2= input("diga o nome do segundo time: ")
gols_time2= int(input("diga quantos gols o segundo time fez: "))

if gols_time1 > gols_time2:
    print(f"o time vencedor é: {time1}")
else:
    if gols_time1 == gols_time2:
        print("EMPATE")
    else:
        print(f"o time vencedor é: {time2}")