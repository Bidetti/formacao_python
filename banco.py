saldo = 0
LIMITE = 500
saques_diarios = 3
extrato_list = []

def deposit(valor):
    global saldo
    if valor < 0:
        print("===============ERROR===============\nValor inválido\n===============ERROR===============")
        return
    saldo += valor
    extrato_list.append("Depósito de R$ %.2f" % valor + " - Saldo após o depósito: R$ %.2f" % saldo)
    print("===============SUCCESS===============\nDepósito realizado com sucesso\n===============SUCCESS===============")


def saque(valor):
    global saldo, saques_diarios
    if saques_diarios == 0:
        print("===============ERROR===============\nVocê já realizou o limite de saques de "
              "hoje.\n===============ERROR===============")
        return
    else:
        if valor < 0:
            print("===============ERROR===============\nValor inválido\n===============ERROR===============")
            return
        elif valor > LIMITE:
            print("===============ERROR===============\nSaque acima do limite\n===============ERROR===============")
            return
        elif valor > saldo:
            print("===============ERROR===============\nSaldo insuficiente\n===============ERROR===============")
            return
        saldo -= valor
        saques_diarios -= 1
        extrato_list.append("Saque de R$ %.2f" % valor + " - Saldo após o saque: R$ %.2f" % saldo)
        print("===============SUCCESS===============\nSaque realizado com sucesso\n===============SUCCESS===============")


def extrato():
    print("====================EXTRATO====================")
    if len(extrato_list) == 0:
        print("Não foram realizadas operações")
    for i in extrato_list:
        print(i)
    print("===============================================")
    print("Saldo atual: R$ %.2f" % saldo)
    print("====================EXTRATO====================")


while True:
    print("D - Depositar")
    print("S - Sacar")
    print("E - Extrato")
    print("Q - Sair")
    opcao = input("Escolha qual operação você deseja: ")
    if opcao == "D" or opcao == "d":
        valor = float(input("Digite o valor do depósito: "))
        deposit(valor)
    elif opcao == "S" or opcao == "s":
        valor = float(input("Digite o valor do saque: "))
        saque(valor)
    elif opcao == "E" or opcao == "e":
        extrato()
    elif opcao == "Q" or opcao == "q":
        break
    else:
        print("===============ERROR===============\nOperação inválida, por favor digite novamente a operação desejada\n===============ERROR===============")
