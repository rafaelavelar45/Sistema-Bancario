menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

saldo = 0
sacar = 0
extrato = ''
limite = 500
numero_saques = 0
LIMITE_SAQUE = 3
extrato_op = []

while True:
    opcao = int(input(menu))

    if opcao == 1:
        deposito = ""
        while True:
            print('======DEPOSITO BANCARIO======')
            deposito = float(input("Digite valor para deposito: "))
            if deposito < 0:
                print("Valor invalido pelo sistema , Tente novamente!")
            else:
                saldo += deposito
                extrato_op.append(f"DEPOSITO REALIZADO NO VALOR DE: R${deposito:.2f}")
                print(f"""
              ==========CONTA BANCARIA==========
              
                  DEPOSITO REALIZADO COM SUCESSO!
              
                  VALOR DEPOSITADO R${deposito:.2f}

                  SALDO R$: {saldo}
              ==================================
                 """)
                break
    elif opcao == 2:
        while  LIMITE_SAQUE >= numero_saques:
                print("========SAQUE BANCARIO==========")
                print(f"SALDO: R${saldo:.2f}")
                print("LIMITE POR SAQUE: R$500")
                print("LIMITE DIARIO DE SAQUE 3")
                sacar =  float(input("VALOR DO SAQUE: "))
                if sacar > saldo or sacar < 0:
                    print("NÃO EXISTE VALOR DISPONIVEL PARA SAQUE.")
                    break
                else:
                    if sacar > limite:
                        print("VALOR EXCEDIDO DE SAQUE POR OPERAÇÃO:")
                        break
                    else: 
                        saldo -= sacar
                        extrato_op.append(f"SAQUE REALIZADO NO VALOR DE: R${sacar}")
                        print("=========================")
                        print(f"SALDO: R${saldo:.2f}")
                        print(f"SAQUE REALIZADO NO VALOR DE R${sacar}")
                        numero_saques += 1
                        break
        if numero_saques > LIMITE_SAQUE:
            print("LIMITE DE SAQUE EXCEDIDO.")
        else:
            print("Obrigado por usar nosso sistema!")
                          
    elif opcao == 3:
        print("==========EXTRATO BANCARIO============")
        for extrato in extrato_op:
            print(extrato)
        
        
        print("=======================================")
    elif opcao == 4:
        break
    else:
        print('Operação invalida , tente novamente!')
