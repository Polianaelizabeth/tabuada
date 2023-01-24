valorIn = float(input("Digite o valor: "))
categoria = int(input("Digite a categoria (1 – limpeza; 2 – alimentação; ou 3 – vestuário): "))
situacao = str(input(" Digite a situação (R – necessitam de refrigeração; e N –não necessitam de refrigeração)"))

if valorIn <= 25:
    if categoria == 1:
        aumento = valorIn*0.05
    elif categoria == 2:
        aumento = valorIn*0.08
    else:
        aumento = valorIn*0.1
else:
    if categoria == 1:
        aumento = valorIn * 0.12
    elif categoria == 2:
        aumento = valorIn * 0.15
    else:
        aumento = valorIn * 0.18

if categoria == 2 or situacao == "R":
    imposto = (valorIn + aumento) * 0.05
else:
    imposto = (valorIn + aumento) * 0.08

valorF = valorIn + aumento - imposto

if valorF <= 50:
    classificacao = "barato"
elif 50 > valorF < 120:
    classificacao = "normal"
else:
    classificacao = "caro"

print("valor inicial: R$", valorIn, "aumento: R$", aumento, "imposto: R$", imposto, "preço final: R$", valorF, "classificaçao: ", classificacao)
