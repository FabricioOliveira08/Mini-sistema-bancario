from biblioteca import criar_conta
from biblioteca import consultar_saldo
from biblioteca import depositar
from biblioteca import sacar

dadosClientes = []

while True:
    print("\n--------MENU--------")
    print("1 - Criar conta")
    print("2 - Consultar Saldo")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if(opcao == 1):
        numeroConta = int(input("\nDigite o número da conta: "))
        novaConta = criar_conta(dadosClientes, numeroConta)

    elif(opcao == 2):
        numeroConta = int(input("\nDigite o número da conta para consultar o saldo: "))

        consultarSaldo = consultar_saldo(dadosClientes, numeroConta)

    elif(opcao == 3):
        numero = int(input("\nDigite o número da conta para depositar: "))

        valor = float(input("\nDigite o valor a ser depositado: "))

        depositarValor = depositar(dadosClientes, numero, valor)

    elif(opcao == 4):
        numero = int(input("\nDigite o número da conta para sacar: "))

        valor = float(input("\nDigite o valor que deseja sacar: "))

        sacarValor = sacar(dadosClientes, numero, valor)
    elif(opcao == 5):
        print("\nSaindo do sistema. Volte sempre!")
        break
    else:
        print("\nOpção inválida. Selecione uma opção válida no menu!")