ano_inicio = int(2000)
ano_final = int(2018)
salario_inicial = float(100)
percentual = float(0.0015)

for i in range(ano_inicio, ano_final, 1):
    if i == 2000:
        print(i, "salario: RS ", salario_inicial)
    elif i == 2001:
        aumento = percentual*salario_inicial
        salario_final = salario_inicial+aumento
        print(i, "SI: RS", salario_inicial, "%: ", percentual, "aumento: RS ", round(aumento, 2), "SF: RS ",
              round(salario_final, 2))
    else:
        print(i, "SI: RS ", round(salario_final, 2))
        percentual *=2
        aumento = percentual*salario_final
        salario_final = salario_final + aumento
        print(i, "SI: RS", round(salario_final, 2), "%: ", percentual, "aumento: RS ", round(aumento, 2), "SF: RS ",
              round(salario_final, 2))
