import textwrap


def menu():
    menu = """\n
        ====================MENU====================
        [D]\tDepositar
        [S]\tSacar
        [E]\tExtrato
        [NC]\tCriar nova conta
        [LC]\tListar contas
        [NU]\tCriar novo usuário
        [Q]\tSair
        => """
    return (input(textwrap.dedent(menu)))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito de R$ {valor:.2f}"
        print(
            "===============SUCCESS===============\nDepósito realizado com sucesso\n===============SUCCESS===============")
    else:
        print("===============ERROR===============\nValor inválido\n===============ERROR===============")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_de_saques, limite_de_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_limite_de_saques = numero_de_saques == limite_de_saques

    if excedeu_saldo:
        print("===============ERROR===============\nSaldo insuficiente\n===============ERROR===============")
    elif excedeu_limite:
        print("===============ERROR===============\nSaque acima do limite\n===============ERROR===============")
    elif excedeu_limite_de_saques:
        print(
            "===============ERROR===============\nVocê já realizou o limite de saques de hoje.\n===============ERROR===============")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque de R$ {valor:.2f}"
        numero_de_saques += 1
        print(
            "===============SUCCESS===============\nSaque realizado com sucesso\n===============SUCCESS===============")
    else:
        print("===============ERROR===============\nValor inválido\n===============ERROR===============")
    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print("====================EXTRATO====================")
    print("Não foram realizadas operações" if not extrato else extrato)
    print(f"Saldo atual: R$ {saldo:.2f}")
    print("====================EXTRATO====================")


def criar_usuario(usuarios):
    cpf = input("Digite o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("===============ERROR===============\nCPF já cadastrado\n===============ERROR===============")
        return

    nome = input("Digite o nome do usuário: ")
    data_de_nascimento = input("Digite a data de nascimento do usuário (dd/mm/aaaa): ")
    endereco = input("Digite o endereço do usuário (Logradouro, num - Bairro - Cidade/Estado: ")

    usuarios.append({"nome": nome, "cpf": cpf, "data_de_nascimento": data_de_nascimento, "endereco": endereco})
    print(
        "===============SUCCESS===============\nUsuário cadastrado com sucesso\n===============SUCCESS===============")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        conta = {
            "agencia": agencia,
            "numero_conta": numero_conta,
            "usuario": usuario
        }
        print("===============SUCCESS===============\nConta criada com sucesso\n===============SUCCESS===============")
        return conta

    print("===============ERROR===============\nUsuário não encontrado\n===============ERROR===============")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            Número da Conta Corrente:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_DE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_de_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "D" or opcao == "d":
            valor = float(input("Digite o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "S" or opcao == "s":
            valor = float(input("Digite o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_de_saques=numero_de_saques,
                limite_de_saques=LIMITE_DE_SAQUES
            )
        elif opcao == "E" or opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "NU" or opcao == "nu":
            criar_usuario(usuarios)
        elif opcao == "NC" or opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)
        elif opcao == "LC" or opcao == "lc":
            listar_contas(contas)
        elif opcao == "Q" or opcao == "q":
            print("Finalizando o sessão...")
            break;

main()