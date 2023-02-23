
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(menu)

    if opcao == "d":
        valor = int(input("Quanto quer depositar? "))
        if valor > 0:
            saldo += valor
            print(f"Valor de R$ {valor}.00 foi depositado.")
            extrato += f"Depósito de R$ {valor}.00 \n"
        else:
            print("Valor inválido!")

    elif opcao == "s":
        if numero_saques == LIMITE_SAQUES:
            print("Conta com 3 saques executados! Novo saque permitido em 24 horas.")
        else:
            valor = int(input("Quanto quer sacar?"))
            if valor <= 500:
                if saldo > valor:
                    saldo -= valor
                    numero_saques += 1
                    extrato += f"Saque de R$ {valor}.00 \n"
                    print(f"Saque permitido no valor de R$ {valor}.00")
                else:
                    print("Valor do saldo insuficiente!")
            else:
                print("Não é permitido valores maiores que R$ 500.00 para saque!")

    elif opcao == "e":
        print(extrato)
        print()
        print(f"Seu saldo atual é de R$ {saldo}.00")

    elif opcao == "q":
        break

    else:
        print("Operação inválida! Por favor selecione novamente a operação desejada.")
