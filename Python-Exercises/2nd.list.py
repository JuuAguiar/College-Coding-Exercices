#Segunda Lista de Exercícios - Python
#Funções

print("Exercicio 1")
#1. Imprimir seu nome com uma letra por linha
def imprimir_nome_linhas(nome):
    for letra in nome:
        print(letra)    
nome = input("Digite seu nome: ")
imprimir_nome_linhas(nome)
print()

print("Exercicio 2")
#2. Escreva uma função que receba uma string e conte o número de vogais dentro dela, 
# por exemplo: entrada: 'Ciência de Dados' saída: 'A palavra tem 7 vogais'
def contar_vogais(string):
    vogais = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vogais:
            count += 1
    return count    
entrada = input("Digite uma string: ")
vogais = contar_vogais(entrada)
print(f"A palavra tem {vogais} vogais")
print()

print("Exercicio 3")
#3) Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' , '−' e '| '. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual 
# a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, eles devem ser modificados para valores 
# dentro da faixa de forma elegante.

def desenhar_moldura(linhas=1, colunas=1):
    linhas = max(1, min(linhas, 20))
    colunas = max(1, min(colunas, 20))
    
    print('+' + '-' * colunas + '+')
    for _ in range(linhas):
        print('|' + ' ' * colunas + '|')
    print('+' + '-' * colunas + '+')
linhas = int(input("Digite o número de linhas (1-20): "))
colunas = int(input("Digite o número de colunas (1-20): "))     
desenhar_moldura(linhas, colunas)
print()

print("Exercicio 4")
#4. Crie um função que retorna o resto de uma divisão

def resto_divisao(a, b):
    return a % b
num1 = int(input("Digite o dividendo: "))
num2 = int(input("Digite o divisor: "))
resto = resto_divisao(num1, num2)
print(f"O resto da divisão de {num1} por {num2} é: {resto}")
print()

print("Exercicio 5")
#5. Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, 
# assim como a quantidade de dias pelos quais o carro foi alugado. 
# Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km_percorridos = float(input("Digite a quantidade de km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias alugados: "))    
custo_total = (dias_alugados * 60) + (km_percorridos * 0.15)
print(f"O preço total a pagar é: R$ {custo_total:.2f}")
print()

print("Exercicio 6")
#6) Escreva um programa para calcular a redução do tempo de vida de um fumante. 
# Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. 
# Considere que um fumante perde 10 minutos de vida a cada cigarro, 
# e calcule quantos dias de vida um fumante perderá. Exiba o total em dias.

cigarros_por_dia = int(input("Digite a quantidade de cigarros fumados por dia: "))
anos_fumados = int(input("Digite quantos anos você já fumou: "))
minutos_perdidos = cigarros_por_dia * 10 * 365 * anos_fumados
dias_perdidos = minutos_perdidos / (24 * 60)
print(f"Você perderá {dias_perdidos:.0f} dias de vida.")
print()

print("Exercicio 7")
#7) Validar e corrigir número de telefone.
# Faça um programa que leia um número de telefone, e corrija o número no caso deste conter somente 7 dígitos, 
# acrescentando o '3' na frente. O usuário pode informar o número com ou sem o traço separador

telefone = input("Digite o número de telefone (7 ou 8 dígitos, com ou sem traço): ")
telefone = telefone.replace("-", "")
if len(telefone) == 7:
    telefone = '3' + telefone
print(f"Número de telefone corrigido: {telefone}")
print()

print("Exercicio 8")
#8) Faça uma função Calculadora que recebe uma expressão matemática e retorna o resultado
#Ex:
# Entrada: Digite uma expressão matemática: 4+5
# Saída: O resultado é 9

def calculadora(expressao):
    try:
        resultado = eval(expressao)
        return resultado    
    except Exception as e:
        return f"Erro na expressão: {e}"
expressao = input("Digite uma expressão matemática: ")
resultado = calculadora(expressao)
print(f"O resultado é: {resultado}")
print()

