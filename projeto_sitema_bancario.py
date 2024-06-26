menu = """"
=========== menu ===========
   [d] depositar
   [s] sacar
   [e] ver extrato
   [x] sair
 =========== Escolha a opção desejada ===========
"""
saldo = 0 
extrato = ""
numero_de_saques = 0 # quantidade realizada no dia 
limite_de_valor = 500 #por saque 
LIMITE_MAXIMO_SAQUE = 3  #por dia 

while True:
    opcao = input(menu)

    if opcao == "d": #realizar deposito
        valor = float (input("Informe o valor que deseja depositar: "))
        if valor > 0:
            saldo += valor 
            extrato +=f"O valor depositado foi : R$ {valor:.2f}\n"
            print(f"valor do deposito foi de R$: {valor}")

        else:
            print("Erro na opração!, por favor informe um valor valido")

    elif opcao == "s": # realizar saque
        valor = float(input("informe o valor que deseja sacar: "))

        ultrapassou_saldo_da_conta = valor > saldo
        ultrapassou_valor_de_saque = valor > limite_de_valor
        ultrapassou_limite_de_saque  = numero_de_saques > LIMITE_MAXIMO_SAQUE

        if ultrapassou_saldo_da_conta: # saldo insuficiente 
            print("erro na operação! saldo insuficiente")
        
        elif ultrapassou_valor_de_saque:  #valor definido por saque e de 500
            print("erro na operação! o valor do saque ultrapassa o limite definido por saque")
        
        elif ultrapassou_limite_de_saque: # limite de saque por dia e de 3 
            print("erro na operação! limite de saque diário atingido.")
        
        elif valor > 0:
            saldo -= valor 
            extrato += f"O valor sacado foi R$: {valor:.2f}\n"
            numero_de_saques += 1 # faz a soma de saques realizado
            print(f"O valor sacado foi R$: {valor}")
        else:
            print("Erro na opração!, por favor informe um valor valido")
    elif opcao == "e":
        print("\n-------------- Extrato --------------")
        print("Não foi realizada nenhuma movimentação nesta conta" if not extrato else extrato)  # caso nao tenha realaizado nenhuma operaçao ate agora 
        print(f"\nO saldo total desta conta e R$ {saldo:.2f}")
        print("---------------------------------------")
    elif opcao == "x": # sair 
        print("obrigado por utilizar nossos serviços, volte sempre.")
        break
    else:
        print("erro na opração!, a operação selecionada e invalida! por favor escolha uma operação valida")