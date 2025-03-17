import random

contas = []

class Conta ():
    def __init__(self, numeroConta, nome):
        self.__numeroConta = numeroConta 
        self.__saldo = 0
        self.__nome = nome
        
        conta = {"numeroConta": self.__numeroConta, 
                "nome":self.__nome, 
                "saldo":self.__saldo
                }
        
        contas.append(conta)
        print(f"Sua conta foi criada com sucesso !! \n Conta: {numeroConta} - {nome}")
    
    def get_numeroConta(self):
        return self.__numeroConta
    
    def get_saldo(self):
        return self.__saldo
    
    def get_nome(self):
        return self.__nome
    
    def depositar(self,numeroConta,valorDepositado):
        if valorDepositado > 0:
            for conta in contas:
                if conta["numeroConta"] == numeroConta:
                    conta["saldo"] += valorDepositado
                    print(f"O valor {valorDepositado} foi depositado com sucesso na conta {numeroConta}")
                    return
            print("Verificar o número da conta!!")
        else:
            print("Favor verificar o valor a ser depositado!")
    
    def sacar(self,numeroConta ,valorSacado):
        if valorSacado > 0:
            for conta in contas:
                if conta["numeroConta"] == numeroConta:
                    if conta["saldo"] > valorSacado:
                        conta["saldo"] -= valorSacado
                        print(f"O valor {valorSacado} foi sacado com sucesso da conta {numeroConta}")
                        return
                    else:
                        print("Saldo Insuficiente")
            print("Verificar se o número da conta!!")
        else:
            print("Favor verificar o valor a ser sacado")
    
    
    def consultarSaldo(self,numeroConta):
        for conta in contas:
            if conta["numeroConta"] == numeroConta:
                print(f"Conta: {conta['numeroConta']} - {conta['nome']} Saldo: R${conta['saldo']}")
                return
        print("Conta não existente")

    def consultarContas(self):
        for conta in contas:
                print(f"Conta: {conta['numeroConta']} - {conta['nome']}")
        return



class Inicio():
        def __init__(self):
            self.conta = None

        def acesso(self):
            while True:
                print("\n Bem vindo ao Caixa Eletronico \n")
                print("1 - Criar uma nova conta")
                print("2 - Depositar valor na conta")
                print("3 - Sacar valor da conta")
                print("4 - Consultar Saldo")
                print("5 - Consultar Contas existentes")
                print("6 - Sair\n")
                escolha = input("O que deseja fazer hoje na sua conta: ")
                if escolha == "1":
                    nome = input("Qual nome da conta? ")
                    numeroConta = random.randint(1, 100)
                    depositoInicial = input("Deseja já realizar algum deposito inicial? \n 1 - Sim\n 2- Não \n ")
                    self.conta = Conta(numeroConta, nome)
                    if depositoInicial == "1":
                        valorDepositado = valorDepositado = float(input("Qual será o valor depositado?"))
                        self.conta.depositar(numeroConta, valorDepositado)
                elif escolha == "2":
                    numeroConta = int(input("Qual o número da conta em que será depoisitado o valor? "))
                    valorDepositado = float(input("Qual será o valor depositado?"))
                    self.conta.depositar(numeroConta,valorDepositado)             
                elif escolha == "3":
                    numeroConta = int(input("Qual o número da conta em que será sacado o valor? "))
                    valorSacado = float(input("Qual o valor que será sacado?"))
                    self.conta.sacar(numeroConta ,valorSacado)
                elif escolha == "4":
                    numeroConta = int(input("Qual o número da conta? "))
                    self.conta.consultarSaldo(numeroConta)
                elif escolha == "5":
                    self.conta.consultarContas()
                elif escolha == "6":
                    print("Encerrando sessão caixa eletronico ...")
                    break
                else:
                    print("Opção invalida, favor tentar novamente")

print("Acesso encerrado, Obrigado !!")
acesso = Inicio()
acesso.acesso()