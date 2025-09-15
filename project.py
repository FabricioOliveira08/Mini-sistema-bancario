from biblioteca import carregar_dados
from biblioteca import salvar_dados
from biblioteca import criar_conta
from biblioteca import consultar_saldo
from biblioteca import depositar
from biblioteca import sacar
from biblioteca import listar_contas
from biblioteca import numero_conta

dadosClientes = carregar_dados("contas.json")

while True:
    print("\n--------MENU--------")
    print("1 - Criar conta")
    print("2 - Consultar Saldo")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Listar contas")
    print("6 - Sair")

    opcao = int(input("\nEscolha uma opção: "))

    if(opcao == 1):
        criar_conta(dadosClientes)

    elif(opcao == 2):
        numeroConta = numero_conta()
        consultarSaldo = consultar_saldo(dadosClientes, numeroConta)

    elif(opcao == 3):
        numeroConta = numero_conta()
        valor = float(input("\nDigite o valor a ser depositado: "))

        depositar(dadosClientes, numeroConta, valor)

    elif(opcao == 4):
        numeroConta = numero_conta()

        valor = float(input("\nDigite o valor que deseja sacar: "))

        sacar(dadosClientes, numeroConta, valor)

    elif(opcao == 5):
        print("\nCONTAS CADASTRADAS: ")
        listar_contas(dadosClientes)

    elif(opcao == 6):
        print("\nSaindo do sistema. Volte sempre!")
        break
    else:
        print("\nOpção inválida. Selecione uma opção válida no menu!")

salvar_dados(dadosClientes, "contas.json")