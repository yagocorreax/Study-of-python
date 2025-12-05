salario_mes1 = int(input("Digite seu salário do primeiro mês:"))
salario_mes2 = int(input("Digite seu salário do segundo mês:"))
if salario_mes1 > salario_mes2:
    print('salário do mês primeiro mês foi maior que o sucessor!')
elif salario_mes1 < salario_mes2:
    print("salário do segundo mês foi maior que o antecessor!")
else:
    print("os salários foram iguais")