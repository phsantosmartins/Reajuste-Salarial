#Perguta ao usuário a quatidade de quilômetros percorridos e armazena em km_percorrido
km_percorrido = float(input("Digite a quantidade de quilometros percorridos: "))
#Pergunta ao usuário a quantidade de dias do aluguel e armazena em aluguel_dias
aluguel_dias = int(input("Digite a quantidade de dias do aluguel: "))

#multiplica o preço com base nos quilômetros percorridos
preco_km = km_percorrido * 0.15
#Muliplica o preço com base nos dias de aluguel
preco_dias = aluguel_dias * 60
#Soma os preços com os quilômetros percorridos com os dias alugados
total = preco_km + preco_dias

print() #imprime uma linha em branco para a melhor visibilidade

#imprime o preço a ser pago pelos os dias alugados
print(f"Preço a pagar pelos os dias: {preco_dias}\n")
#Indica o preço a ser pago pelos quilômetros rodados
print(f"Preço a pagar pelos quilometros rodados: {preco_km}\n")
#Imprime o valor total a ser pago
print(f"Total a ser pago: {total}")


