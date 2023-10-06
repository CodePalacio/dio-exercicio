menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor = float(input("Que quantia deseja depositar?"))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito: R$ {valor:.2}\n'
        else:
            print('O valor digitado é invalido')
    
    elif opcao == 's':
        valor = float(input('Informe o valor do saque'))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print('Operação falhou. Voce nao tem saldo suficiente')
        
        elif excedeu_limite:
            print('Operação falhou. Voce excedeu seu limite')

        elif excedeu_saques:
            print('Operação falhou. Voce excedeu seu limite de saques')
        
        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: R$ {valor:.2f}'
            numero_saques += 1

        else: 
            print('Operação falhou! Valor informado invalido')
    
    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")