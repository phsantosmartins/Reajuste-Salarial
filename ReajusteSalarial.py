#Reajuste Salarial
#Define um loop para que o código se repita até o usuário encerrar o programa
while True:
    #Solocita que o usuário entre com o seu salário
    salario = float(input("Digite o seu salário (ou digite 0 para encerra): "))
    #Verifica se o usuário digitou 0 para encerrar o programa
    if salario == 0:
        print("Programa encerrado.")
        break

        #Calcula o aumento do salário em 15%
    aumento = salario + (salario * 0.15) 
    
    #Exibe o novo salário
    print("Seu salário com um aumento de 15% passa a ser {} reais" .format(aumento))


