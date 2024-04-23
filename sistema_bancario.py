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
        valor = float(input("Digite o valor a ser depositado: "))

        if valor > 0:
            saldo += valor
            extrato += "Depósito de R$ {:.2f}\n".format(valor)
        else:
            print("Operação falhou! Valor inválido")


    elif opcao == "s":
        valor = float(input("Digite o valor a ser sacado: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Saldo insuficiente")
        elif excedeu_limite:
            print("Operação falhou! Limite excedido")
        elif excedeu_saques:
            print("Operação falhou! Limite de saques excedido")

        elif valor > 0:
            saldo -= valor
            extrato += "Saque de R$ {:.2f}\n".format(valor)
            numero_saques += 1
        else:
            print("Operação falhou! Valor inválido")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação falhou! Opção inválida")        

      