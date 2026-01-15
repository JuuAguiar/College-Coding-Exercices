#Lista de exercícios – POO em Python


#1. Altere a classe ContaBancaria adicionando uma lista operacoes (como atributo da classe)
#para registrar todas as operações de depósito e saque.
#Crie um método extrato para listar todas as operações realizadas.

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append(f"Depósito: R$ {valor:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.operacoes.append(f"Saque: R$ {valor:.2f}")
        else:
            self.operacoes.append("Tentativa de saque sem saldo suficiente")

    def extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for op in self.operacoes:
            print(op)


print()


#2. Altere o método extrato de ContaBancaria de forma que o saldo
#seja impresso após cada operação (saque / depósito).

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self.operacoes = []

    def depositar(self, valor):
        self.saldo += valor
        self.operacoes.append((f"Depósito: R$ {valor:.2f}", self.saldo))

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            self.operacoes.append((f"Saque: R$ {valor:.2f}", self.saldo))
        else:
            self.operacoes.append(("Tentativa de saque sem saldo suficiente", self.saldo))

    def extrato(self):
        print(f"Extrato da conta de {self.titular}:")
        for op, saldo in self.operacoes:
            print(f"{op} | Saldo após operação: R$ {saldo:.2f}")


conta = ContaBancaria("João", 500)
conta.depositar(300)
conta.sacar(200)
conta.sacar(800)
conta.extrato()
print()


#3. Crie uma classe Banco que tem como atributos o nome do banco,
#uma lista com os nomes dos clientes e uma lista com os respectivos números das contas.
class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []


print()


#4. Crie um método para classe Banco chamado abrir_conta
#que faz append nas listas e cria uma nova instância de ContaBancaria.

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abrir_conta(self, nome_cliente, saldo_inicial=0):
        conta = ContaBancaria(nome_cliente, saldo_inicial)
        self.clientes.append(nome_cliente)
        self.contas.append(conta)
        return conta


print()


#5. Crie um método para o Banco chamado lista_contas
#para imprimir as contas e respectivo saldo.

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abrir_conta(self, nome_cliente, saldo_inicial=0):
        conta = ContaBancaria(nome_cliente, saldo_inicial)
        self.clientes.append(nome_cliente)
        self.contas.append(conta)
        return conta

    def lista_contas(self):
        print(f"Contas do banco {self.nome}:")
        for conta in self.contas:
            print(f"Cliente: {conta.titular} | Saldo: R$ {conta.saldo:.2f}")

#6. Crie um método para o Banco para listar as contas com saldo superior a 10000.

class Banco:
    def __init__(self, nome):
        self.nome = nome
        self.clientes = []
        self.contas = []

    def abrir_conta(self, nome_cliente, saldo_inicial=0):
        conta = ContaBancaria(nome_cliente, saldo_inicial)
        self.clientes.append(nome_cliente)
        self.contas.append(conta)
        return conta

    def lista_contas(self):
        print(f"Contas do banco {self.nome}:")
        for conta in self.contas:
            print(f"Cliente: {conta.titular} | Saldo: R$ {conta.saldo:.2f}")

    def contas_saldo_superior_10000(self):
        print("Contas com saldo superior a R$ 10.000:")
        for conta in self.contas:
            if conta.saldo > 10000:
                print(f"Cliente: {conta.titular} | Saldo: R$ {conta.saldo:.2f}")


banco = Banco("Banco Central Python")
banco.abrir_conta("Ana", 5000)
banco.abrir_conta("Carlos", 15000)
banco.abrir_conta("Beatriz", 25000)

banco.lista_contas()
print()
banco.contas_saldo_superior_10000()

