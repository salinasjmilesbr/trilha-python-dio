# Edição por salinasjmilesbr

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
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
 
        else:
            print("Operação falhou! O valor informado é inválido.")   

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        execedeu_saldo = valor > saldo

        execedeu_limite = valor > limite

        execedeu_saques = numero_saques >= LIMITE_SAQUES

        if execedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif execedeu_limite:
            print("Operação falhou! O valor excede o limite de R$500,00.") 

        elif execedeu_saques:
            print("Operação falhou! Você excedeu o limite de 3 saques.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n============ EXTRATO ============")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("===================================")

    elif opcao == "q":
        break

    else:
        print("Operação Inválida! Por favor selecione a opção desejada.")