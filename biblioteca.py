
def criar_conta(lista_clientes, numeroConta):
    
    for cliente in lista_clientes:
        if(cliente['numeroConta'] == numeroConta):
            print("Conta já existente!")
            break
    
    nomeCliente = input("Digite o nome do cliente: ")
    saldo = float(input("Digite o saldo inicial: "))

    cliente = {
            "nomeCliente": nomeCliente,
            "numeroConta": numeroConta,
            "saldo": saldo
        }
    lista_clientes.append(cliente)

    print(f"\nConta de {nomeCliente} criada com sucesso.")
    return True


def consultar_saldo(lista_clientes, numero):

    for cliente in lista_clientes:
        if(cliente["numeroConta"] == numero):
            print(f"\nCliente: {cliente['nomeCliente']} | Saldo: R${cliente['saldo']:.2f}")
            return True
    
    print("\nConta não encontrada.")
    return False


def depositar(lista_clientes, numero, valor):
     
    for cliente in lista_clientes:
        if(cliente['numeroConta'] == numero):
            if(valor > 0):
                cliente['saldo'] += valor
                print("\nDeposito concluído com sucesso.")
            else:
                print("Valor inválido para depósito.")
            return True
            
    print("\nConta não encontrada.")
    return False


def sacar(lista_clientes, numero, valor):
    for cliente in lista_clientes:
        if(cliente['numeroConta'] == numero):
            if(valor > 0):
                if(cliente['saldo'] >= valor):  
                    cliente['saldo'] -= valor
                    print("\nSaque concluído com sucesso.")
                else:
                    print("\nSaldo insuficiente para realizar saque.")
            else: 
                print("Valor inválido para saque.")
            return True    
        
    print("\nConta não encontrada.")
    return False