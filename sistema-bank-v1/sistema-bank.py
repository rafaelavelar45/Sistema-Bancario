import os
import re

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

clear_screen()
menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Seja cliente , abra sua conta corrente agora
[5] Meus Clientes NU
[6] Cliente cadastrados
[7] Sair
"""



extrato = ''
limite = 500
LIMITE_SAQUE = 3
extrato_op = []
cliente = []
cliente_logado = None

def deposito_conta( cliente_logado):
    deposito = ""
    if cliente_logado == None:
        print("Entre em uma conta para continuar")
    else:
      while True:
            print('======DEPOSITO BANCARIO======')
            print(f'Olá {cliente_logado["nome"]}')
            deposito = float(input("Digite valor para deposito: "))
            if deposito < 0:
                print("Valor invalido pelo sistema , Tente novamente!")
            else:
                cliente_logado["saldo"] += deposito
                extrato_op.append(f"DEPOSITO REALIZADO NO VALOR DE: R${deposito:.2f}")
                clear_screen()

                print(f"""
              ==========CONTA BANCARIA==========
              
                  DEPOSITO REALIZADO COM SUCESSO!
              
                  VALOR DEPOSITADO R${deposito:.2f}

                  SALDO R$: {cliente_logado["saldo"]}
              ==================================
                 """)
                break
            return cliente_logado
def saque_conta(cliente_logado, extrato_op,*, LIMITE_SAQUE= 3, limite= 500,):
    if cliente_logado == None:
        print("Não e possivel accessar este serviço , entre em uma conta") 
    else:
        while cliente_logado["numero_saques"] < LIMITE_SAQUE:
                print("========SAQUE BANCARIO==========")
                print(f"SALDO: R${cliente_logado["saldo"]:.2f}")
                print("LIMITE POR SAQUE: R$500")
                print("LIMITE DIARIO DE SAQUE 3")
                sacar =  float(input("VALOR DO SAQUE: "))
                if sacar > cliente_logado["saldo"] or sacar < 0:
                    print("NÃO EXISTE VALOR DISPONIVEL PARA SAQUE.")
                    break
                else:
                    if sacar > limite:
                        print("VALOR EXCEDIDO DE SAQUE POR OPERAÇÃO:")
                        break
                    else: 
                        cliente_logado["saldo"] -= sacar
                        extrato_op.append(f"SAQUE REALIZADO NO VALOR DE: R${sacar}")
                        print("=========================")
                        print(f"SALDO: R${cliente_logado["saldo"]}")
                        print(f"SAQUE REALIZADO NO VALOR DE R${sacar}")
                        extrato_op.append(f"SALDO DISPONIVEL: R${cliente_logado["saldo"]:.2f}")
                        cliente_logado["numero_saques"] += 1
                    if cliente_logado["numero_saques"] == LIMITE_SAQUE:
                             print("LIMITE DE SAQUE EXCEDIDO.")
                    else:
                             print("Obrigado por usar nosso sistema!")
    return   cliente_logado, extrato_op,  LIMITE_SAQUE, limite


def cadastro_cliente():
    usuario = {
          "nome": input("Nome Completo: "),
          "cpf": input("Digite seu CPF: "),
          "endereço": input("Digite seu endereço: "),
          "saldo": 0,
          "extrato": [],
          "numero_saques": 0
     }
    return usuario

def loguin_usuario(cliente):
    buscar_cpf = input("Digite CPF: ")

    for cliente_existente in cliente:
         
         if cliente_existente["cpf"] == buscar_cpf:
              print(f"Seja Bem-Vindo {cliente_existente["nome"]}")
              return cliente_existente

    print("Cliente nao encontrado")
    return None

         


    
     
     
while True:
    opcao = int(input(menu))
    if opcao == 1:
        
        deposito_conta(cliente_logado) 
    elif opcao == 2:
        cliente_logado, extrato_op, LIMITE_SAQUE, limite = saque_conta( cliente_logado=cliente_logado, extrato_op=extrato_op, LIMITE_SAQUE=LIMITE_SAQUE, limite=limite)
    elif opcao == 3:
        clear_screen()
        if extrato == "":
             print("Não existe operação")
        else:
            print("==========EXTRATO BANCARIO============")
            for extrato in extrato_op:
                print(extrato)
            print("=======================================")
    elif opcao == 4:
        
        novo_cliente = cadastro_cliente()
        cadastro_existente = any(c["cpf"] == novo_cliente["cpf"] for c in cliente)
        if not cadastro_existente:
            if not novo_cliente["cpf"].isdigit() or len(novo_cliente["cpf"]) > 11 or len(novo_cliente["cpf"] ) < 11:
                print("Use digitos neste formato e 11 digitos para um CPF valido.")
            elif re.search(r'\d', novo_cliente["nome"]):
                 print("Nome invalido nao pode conter nuemroe e nem simbolos")
            elif not re.fullmatch(r"[A-Za-zÀ-ÿ\s]+", novo_cliente["nome"]):
                 print("Nome nao pode conter simbolos")
            else:
                 cliente.append(novo_cliente)
                 print("Cliente cadastrado com sucesso!")
        else:
             print("Ja existe um cadastro com esse cpf , faça loguin")
                 
           
                
                 
        
    elif opcao == 5:
         for buscar in cliente:
              print(f"""
                        Cliente: {buscar["nome"]}
                        CPF: {buscar["cpf"]}
                        Endereço: {buscar["endereço"]}
                    """)
    elif opcao == 6:
         cliente_logado = None
         cliente_logado = loguin_usuario(cliente)
    elif opcao == 7:
         print("Obrigado por usar nosso sitema")
         break     
    else:
        clear_screen()
        print('Operação invalida , tente novamente!') 