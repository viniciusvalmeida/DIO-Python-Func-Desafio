saldo = 0
extrato = ""
limite_saque = 500
numero_saque = 0
LIMITE_SAQUE = 3

menu = """
----- MENU -----

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"

    else:
        print("Valor inválido")


def saque(*, saldo=saldo, valor, extrato=extrato, limite=limite_saque, numero_saques=numero_saque, limite_saques=LIMITE_SAQUE):
    if valor > saldo:
        print("\nSaldo insuficiente")

    elif valor > limite:
        print(f"\nLimite de saque no valor de R$ {limite_saque:.2f}")

    elif numero_saques >= limite_saques:
        print("\nNúmero de saques diários atingidos, tente novamente amanhã!")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\nSaque: R$ {valor:.2f}\n"

    else:
        print("Valor inválido")


def extrato(saldo, /, *, extrato=extrato):
    print(" Extrato ".center(21, "-"))
    print(extrato if extrato else "Não foram realizadas movimentações")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(21, "-"))


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))

        saque(valor=valor)

    elif opcao == "e":
        extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor digitar umas das opções acima")
