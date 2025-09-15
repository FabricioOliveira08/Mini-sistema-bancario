import json
#Funções Auxiliares
def nome_cliente():
    while True:
        nomeCliente = input("Digite o nome do cliente: ")
        if(nomeCliente.isdigit()):
            print("Digite um nome válido!")
        else:
            break
    return nomeCliente

def numero_conta():
    
    while True:
        nConta = input("\nDigite o número da conta: ")
        try:
            nContaInt = int(nConta)
            if(nContaInt > 0):
                break
            else:
                print("Digite um número válido.")
        except:
            print("Digite um número válido.")
    
    return nContaInt

def encontrar_cliente(lista_clientes, numeroConta):
    for cliente in lista_clientes:
        if(cliente['numeroConta'] == numeroConta):
            return cliente
    return 
            
#Funções de Lógica
def criar_conta(lista_clientes):

    numeroConta = numero_conta()
    nomeCliente = nome_cliente()
    saldo = float(input("Digite o saldo inicial: "))

    clienteExistente = encontrar_cliente(lista_clientes,  numeroConta)

    if(clienteExistente == None):
        cliente = {
            "nomeCliente": nomeCliente,
            "numeroConta": numeroConta,
            "saldo": saldo
        }
        lista_clientes.append(cliente)
        print(f"\nConta de {nomeCliente} criada com sucesso.")
        return True
    else: 
        print("\nConta já existente.")
        return False


def consultar_saldo(lista_clientes, numeroConta):
    
    clienteExistente = encontrar_cliente(lista_clientes, numeroConta)
    
    if(clienteExistente != None):
        print(f"\nCliente: {clienteExistente['nomeCliente']} | Saldo: R${clienteExistente['saldo']:.2f}")
        return True
    else:  
        print("\nConta não encontrada.")
        return False    


def depositar(lista_clientes, numeroConta, valor):
     
    clienteExistente = encontrar_cliente(lista_clientes, numeroConta)
    
    if(clienteExistente != None):
        if(valor > 0):
            clienteExistente['saldo'] += valor
            print("\nDeposito concluído com sucesso.")
            return True
        else:
            print("\nValor inválido para depósito.")
            return False
    else:       
        print("\nConta não encontrada.")
        return False


def sacar(lista_clientes, numeroConta, valor):
    
    clienteExistente = encontrar_cliente(lista_clientes, numeroConta)
    
    if(clienteExistente != None):
        if(valor > 0):
            if(clienteExistente['saldo'] >= valor):  
                clienteExistente['saldo'] -= valor
                print("\nSaque concluído com sucesso.")
                return True
            else:
                print("\nSaldo insuficiente para realizar saque.")
                return False
        else: 
            print("Valor inválido para saque.")
            return False    
    else:
       print("\nConta não encontrada.")
       return False 
    

def listar_contas(lista_clientes):
    if(len(lista_clientes) == 0):
        print("\nNenhuma conta cadastrada.")
    else:
        for cliente in lista_clientes:
            nome = cliente["nomeCliente"]
            n_conta = cliente["numeroConta"]
            saldo = cliente["saldo"]
            print(f"\nNome: {nome} | Número da conta: {n_conta} | Saldo: R${saldo:.2f}")
    return 

#Funções de Persistência
def carregar_dados(nome_arquivo):
    try:
       with open(nome_arquivo, "r") as arquivo:
            conteudo = arquivo.read()
            lista_clientes = json.loads(conteudo)
            return lista_clientes
    except:
        return []

def salvar_dados(lista_clientes, nome_arquivo):
    with open(nome_arquivo, "w") as arquivo:
        json.dump(lista_clientes, arquivo, indent=4)