class ContaBancaria:
    def __init__(self, numero_conta, nome_titular, saldo_inicial=0, limite_cheque_especial=0, ativa=False):
        self.numero_conta = numero_conta
        self.nome_titular = nome_titular
        self.saldo = saldo_inicial
        self.limite_cheque_especial = limite_cheque_especial
        self.ativa = ativa

    def depositar(self, valor):
        if self.ativa:
            self.saldo += valor
            print(f"Depósito de R${valor} realizado na conta {self.numero_conta}. Saldo atual: R${self.saldo}")
        else:
            print("Não é possível fazer depósito. A conta está desativada.")

    def sacar(self, valor):
        if self.ativa:
            if self.saldo + self.limite_cheque_especial >= valor:
                if self.saldo >= valor:
                    self.saldo -= valor
                else:
                    self.limite_cheque_especial -= (valor - self.saldo)
                    self.saldo = 0
                print(f"Saque de R${valor} realizado na conta {self.numero_conta}. Saldo atual: R${self.saldo}")
            else:
                print(f"Saldo insuficiente na conta {self.numero_conta}. Saque cancelado.")
        else:
            print("Não é possível fazer saque. A conta está desativada.")

    def transferir(self, conta_destino, valor):
        if self.ativa:
            if self.saldo + self.limite_cheque_especial >= valor:
                if self.saldo >= valor:
                    self.saldo -= valor
                else:
                    self.limite_cheque_especial -= (valor - self.saldo)
                    self.saldo = 0
                conta_destino.depositar(valor)
                print(f"Transferência de R${valor} realizada da conta {self.numero_conta} para a conta {conta_destino.numero_conta}.")
            else:
                print(f"Saldo insuficiente na conta {self.numero_conta}. Transferência cancelada.")
        else:
            print("Não é possível fazer transferência. A conta está desativada.")

    def consultar_saldo(self):
        if self.ativa:
            print(f"Saldo na conta {self.numero_conta}: R${self.saldo}")
            print(f"Limite de Cheque Especial na conta {self.numero_conta}: R${self.limite_cheque_especial}")
        else:
            print("A conta está desativada.")

    def ativar_conta(self):
        self.ativa = True
        print(f"A conta {self.numero_conta} foi ativada.")


class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.contas = []

    def adicionar_conta(self, conta):
        self.contas.append(conta)

    def buscar_conta(self, numero_conta):
        for conta in self.contas:
            if conta.numero_conta == numero_conta:
                return conta
        print(f"Conta {numero_conta} não encontrada.")
        return None


def exibir_menu():
    print("----- Menu -----")
    print("1. Criar conta")
    print("2. Depositar")
    print("3. Sacar")
    print("4. Transferir")
    print("5. Consultar saldo")
    print("6. Ativar conta")
    print("7. Sair")


meu_banco = Banco("Meu Banco")

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero_conta = input("Digite o número da conta: ")
        nome_titular = input("Digite o nome do titular da conta: ")
        saldo_inicial = float(input("Digite o saldo inicial da conta: "))
        limite_cheque_especial = float(input("Digite o limite de Cheque Especial da conta: "))

        conta = ContaBancaria(numero_conta, nome_titular, saldo_inicial, limite_cheque_especial)
        meu_banco.adicionar_conta(conta)
        print("Conta criada com sucesso!")

    elif opcao == "2":
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor a ser depositado: "))

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.depositar(valor)

    elif opcao == "3":
        numero_conta = input("Digite o número da conta: ")
        valor = float(input("Digite o valor a ser sacado: "))

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.sacar(valor)

    elif opcao == "4":
        numero_conta_origem = input("Digite o número da conta de origem: ")
        numero_conta_destino = input("Digite o número da conta de destino: ")
        valor = float(input("Digite o valor a ser transferido: "))

        conta_origem = meu_banco.buscar_conta(numero_conta_origem)
        conta_destino = meu_banco.buscar_conta(numero_conta_destino)
        if conta_origem and conta_destino:
            conta_origem.transferir(conta_destino, valor)

    elif opcao == "5":
        numero_conta = input("Digite o número da conta: ")

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.consultar_saldo()

    elif opcao == "6":
        numero_conta = input("Digite o número da conta: ")

        conta = meu_banco.buscar_conta(numero_conta)
        if conta:
            conta.ativar_conta()

    elif opcao == "7":
        print("Obrigado por usar nosso sistema bancário. Volte sempre!")
        break

    else:
        print("Opção inválida. Digite novamente.")