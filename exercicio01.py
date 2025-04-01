nome = input("digite seu nome: ")
idade = int(input("agora digite sua idade: "))
salario = float(input("inorme seu salário: "))
aumento = float(input("informe o percentual de aumento do salário: "))
novosalario = salario * (aumento/100) + salario
print(f"informações:\n{nome}\n{idade}\n{salario}\nR${novosalario}")