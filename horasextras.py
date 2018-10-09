# -*- coding: utf-8 -*-
#Exercicio das horas extras trabalhadas
hrs_trabalhadas = int(input("Insira as horas trabalhadas: "))
salario_hr = input("Digite o salário p/hora: R$ ")

if(hrs_trabalhadas >= 160):
    nv_salario = ((hrs_trabalhadas * salario_hr) + ((salario_hr/100) * 0.5))
    meses_trabalhados = int((hrs_trabalhadas / 160))
    print("Foram trabalhadas {0} horas e o salario do funcionario acrescido das horas extras: R$ {1:.2f}, {2} mes(es) trabalhados.").format(hrs_trabalhadas, nv_salario, meses_trabalhados)
else:
    print("Mes nao foi fechado, foram trabalhados {0} horas, necessario no minimo 40 hrs de trabalho.").format(hrs_trabalhadas)