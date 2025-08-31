dadosClientes = []
# nomeCliente = ""
# numeroConta = 0
# saldo = 0.0

while True:
    print("\n--------MENU--------")
    print("1 - Criar conta")
    print("2 - Consultar Saldo")
    print("3 - Depositar")
    print("4 - Sacar")
    print("5 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if(opcao == 1):
        nomeCliente = input("Digite o nome do cliente: ")
        numeroConta = int(input("Digite o número da conta: "))
        saldo = float(input("Digite o saldo inicial: "))

        cliente = {
            "nomeCliente": nomeCliente,
            "numeroConta": numeroConta,
            "saldo": saldo
        }
        dadosClientes.append(cliente)
         
        print(f"\nConta de {nomeCliente} criada com sucesso.")
    elif(opcao == 2):
        numero = int(input("Digite o número da conta para consultar o saldo: "))

        encontrado = False
        for cliente in dadosClientes:
            if(cliente["numeroConta"] == numero):
                print(f"\nCliente: {cliente['nomeCliente']} | Saldo: R${cliente['saldo']:.2f}")
                encontrado = True
                break
        if(encontrado == False):
            print("\nConta não encontrada.")

    elif(opcao == 3):
        numero = int(input("\nDigite o numero da conta para depositar: "))

        encontrado = False
        for cliente in dadosClientes:
            if(cliente['numeroConta'] == numero):
                deposito = float(input("\nDigite o valor a ser depositado: "))
                cliente['saldo'] += deposito
                print("\nDeposito concluído com sucesso.")
                encontrado = True
                break
        if(encontrado == False):
            print("\nConta não encontrada.")
    elif(opcao == 4):
        numero = int(input("\nDigite o numero da conta para sacar: "))

        encontrado = False
        for cliente in dadosClientes:
            if(numeroConta != 0):
                saque = float(input("\nDigite o valor que deseja sacar: "))
                if(cliente['saldo'] >= saque):  
                    cliente['saldo'] -= saque
                    print("\nSaque concluído com sucesso.")
                else:
                    print("\nSaldo insuficiente para realizar saque.")
                encontrado = True
                break
        if(encontrado == False):
            print("\nConta não encontrada.")
    elif(opcao == 5):
        print("\nSaindo do sistema. Volte sempre!")
        break
    else:
        print("\nOpção inválida. Selecione uma opção válida no menu!")