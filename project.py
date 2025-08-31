nomeCliente = ""
numeroConta = 0
saldo = 0.0

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
        numeroConta = input("Digite o número da conta: ")
        saldo = float(input("Digite o saldo inicial: "))
        print(f"\nConta de {nomeCliente} criada com sucesso.")
    elif(opcao == 2):
        if(numeroConta != 0):
            print(f"\nCliente: {nomeCliente} | Saldo: R${saldo:.2f}")
        else: 
            print("\nConta não encontrada.")
    elif(opcao == 3):
        if(numeroConta != 0):
            deposito = float(input("\nDigite o valor a ser depositado: "))
            saldo += deposito
            print("\nDeposito concluído com sucesso.")
        else:
            print("\nConta não encontrada.")
    elif(opcao == 4):
        if(numeroConta != 0):
            saque = float(input("\nDigite o valor que deseja sacar: "))
            saldo -= saque
            print("\nSaque concluído com sucesso.")
        else:
            print("\nConta não encontrada.")
    elif(opcao == 5):
        print("\nSaindo do sistema. Volte sempre!")
        break
    else:
        print("\nOpção inválida. Selecione uma opção válida no menu!")