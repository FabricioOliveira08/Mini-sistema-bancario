import json
#Funções de Lógica
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
                print("\nValor inválido para depósito.")
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