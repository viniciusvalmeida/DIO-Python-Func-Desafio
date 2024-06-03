AGENCIA = "0001"
LIMITE_SAQUE = 3

saldo = 0
extrato = ""
limite_saque = 500
numero_saques = 0
clientes = []
contas = []

menu = """
----- MENU -----

[d] Depositar
[s] Sacar
[e] Extrato
[c] Criar cliente
[n] Nova conta
[l] Listar contas
[q] Sair

=> """


def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"\nDepósito: \tR$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")

    else:
        print("Valor inválido!")

    return saldo, extrato


def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("\nSaldo insuficiente")

    elif valor > limite:
        print(f"\nLimite de saque no valor de R$ {limite_saque:.2f}")

    elif numero_saques >= limite_saques:
        print("\nNúmero de saques diários atingidos, tente novamente amanhã!")

    elif valor > 0:
        saldo -= valor
        numero_saques += 1
        extrato += f"\nSaque: \tR$ {valor:.2f}\n"
        print(
            f"Saque realizado com sucesso no valor de R$ {valor:.2f}\n\nNúmero de saques restantes: {numero_saques}")

    else:
        print("Valor inválido")

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato=extrato):
    print(" Extrato ".center(21, "-"))
    print(extrato if extrato else "Não foram realizadas movimentações")
    print(f"\nSaldo: \tR$ {saldo:.2f}")
    print("".center(21, "-"))


def criar_cliente(cliente, clientes: list):
    for c in clientes:
        if c["cpf"] == cliente["cpf"]:
            return '\n\nCliente já cadastrado!'

    clientes.append(cliente)
    return f"\n\nBem vindo {cliente['nome']} ao nosso banco!"


def criar_conta(cpf: str):
    numero_conta = len(contas) + 1
    for cliente in clientes:
        if cliente["cpf"] == cpf:
            conta = {"agencia": AGENCIA,
                     "numero_conta": numero_conta, "usuario": cliente}
            contas.append(conta)
            return "\nConta criada com sucesso"

    return "\nCliente não encontrado"


def listar_contas():
    for conta in contas:
        print(f"""
        DONO: {conta["usuario"]["nome"]}
        CPF: {conta["usuario"]["cpf"]}
        NUMERO: {conta["numero_conta"]}
        """)


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Digite o valor a ser depositado: "))

        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Digite o valor para saque: "))

        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato,
                               limite=limite_saque, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)

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
        cpf = input("Digite o CPF do dono da conta: ")

        print(criar_conta(cpf))

    elif opcao == 'l':
        listar_contas()

    elif opcao == "q":
        break

    else:
        print("Opção inválida, por favor digitar umas das opções acima")
