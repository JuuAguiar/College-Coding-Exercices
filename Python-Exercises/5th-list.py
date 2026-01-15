#Quinta lista de exercícios
#POO em Python


#1. Crie uma classe chamada "Retangulo" que tenha os atributos "largura" e "altura".
#Crie métodos para calcular a área e o perímetro do retângulo.
class retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)


ret1 = retangulo(10, 5)
print("Área:", ret1.area())
print("Perímetro:", ret1.perimetro())
print()


#2. Crie uma classe chamada "ContaBancaria" que tenha os atributos "titular" e "saldo".
#Crie métodos para depositar, sacar e exibir o saldo da conta.
class ContaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print("Saldo insuficiente")

    def exibir_saldo(self):
        print(f"Titular: {self.titular} | Saldo: R$ {self.saldo:.2f}")


conta = ContaBancaria("Maria", 200)
conta.depositar(100)
conta.sacar(50)
conta.exibir_saldo()
print()


#3. Crie uma classe chamada "Carro" que tenha os atributos "marca", "modelo" e "ano".
#Crie um método para exibir as informações completas do carro.
class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def exibir_informacoes(self):
        print(f"Marca: {self.marca}, Modelo: {self.modelo}, Ano: {self.ano}")


carro = Carro("Honda", "Civic", 2022)
carro.exibir_informacoes()
print()


#4. Crie uma classe chamada "Cachorro" que tenha os atributos "nome" e "idade".
#Crie um método para exibir o nome e a idade do cachorro e um método para latir.
class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def exibir_dados(self):
        print(f"Nome: {self.nome}, Idade: {self.idade} anos")

    def latir(self):
        print("Au au!")


cachorro = Cachorro("Bob", 3)
cachorro.exibir_dados()
cachorro.latir()
print()


#5. Sobrecarga do método __str__ e comparação de preços
class Produto:
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"Código: {self.codigo}, Nome: {self.nome}, Preço: R$ {self.preco:.2f}"

    def __ge__(self, outro):
        return self.preco >= outro.preco


produto1 = Produto(1, "Camiseta", 79.90)
produto2 = Produto(2, "Calça Jeans", 99.90)

print(produto2)
print("O preço do produto 1 é maior ou igual ao produto 2?", produto1 >= produto2)
print()


#6. Alteração da classe Retangulo
#- Identificar se é quadrado
#- Comparar retângulos
class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def area(self):
        return self.largura * self.altura

    def eh_quadrado(self):
        return self.largura == self.altura

    def __gt__(self, outro):
        return self.area() > outro.area()

    def __lt__(self, outro):
        return self.area() < outro.area()


r1 = Retangulo(4, 4)
r2 = Retangulo(3, 6)

print("r1 é quadrado?", r1.eh_quadrado())
print("r1 é maior que r2?", r1 > r2)
print("r1 é menor que r2?", r1 < r2)
print()