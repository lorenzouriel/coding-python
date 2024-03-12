nome = str(input("Qual é o seu nome?: "))
salario = float(input("Qual é o seu salário?: "))
bonus = float(input("Vi que recebeu um bônus! Pode confirmar a porcentagem?: "))

calculo_bonus = 1000 + salario * bonus

print(f"Olá {nome}, o seu bônus foi de R${calculo_bonus}! Parabéns!")