saldo = 0
extrato = ""
limite_saque = 500
numero_saque = 0
LIMITE_SAQUE = 3
clientes = []
contas = []

menu = """
----- MENU -----

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar cliente
[n] Nova conta
[q] Sair

=> """


def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: R$ {valor:.2f}\n"
        return saldo, extrato

    else:
        print("Valor inválido")
        return False


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nSaldo insuficiente")
        return False

    elif valor > limite:
        print(f"\nLimite de saque no valor de R$ {limite_saque:.2f}")
        return False

    elif numero_saques >= limite_saques:
        print("\nNúmero de saques diários atingidos, tente novamente amanhã!")
        return False

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\nSaque: R$ {valor:.2f}\n"

        return saldo, numero_saques, extrato

    else:
        print("Valor inválido")


def exibir_extrato(saldo, /, *, extrato=extrato):
    print(" Extrato ".center(21, "-"))
    print(extrato if extrato else "Não foram realizadas movimentações")
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("".center(21, "-"))


def criar_cliente(cliente, clientes: list):
    for c in clientes:
        if c["cpf"] == cliente["cpf"]:
            return 'Cliente já cadastrado'

    clientes.append(cliente)
    return f"Bem vindo {cliente["nome"]} ao nosso banco!"


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        res = deposito(saldo, valor, extrato)

        if res:
            saldo = res[0]
            extrato = res[1]

    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))

        res = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite_saque,
                    numero_saques=numero_saque, limite_saques=LIMITE_SAQUE)

        if res:
            saldo = res[0]
            numero_saque = res[1]
            extrato = res[2]

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "c":
        nome = input("Digite o nome do cliente: ")
        data_nascimento = input("Digite a data de nascimento: ")
        cpf = input("Digite o CPF: ")
        logradouro = input("Digite o logradouro: ")
        bairro = input("Digite o bairro: ")
        estado = input("Digite o estado: ")

        cliente = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf,
                   "endereco": {"logradouro": logradouro, "bairro": bairro, "estado": estado}}

        print(criar_cliente(cliente, clientes))

    elif opcao == "n":
        pass

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor digitar umas das opções acima")
