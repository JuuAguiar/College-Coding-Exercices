#Quarta lista de exercícios - Python

#1. Escreva uma função que receba uma lista de strings como argumento e retorne uma nova lista 
# contendo apenas as strings que começam com a letra "a".
def filtrar_strings_com_a(lista):
    return [s for s in lista if s.lower().startswith('a')]
strings = ['abacaxi', 'banana', 'amora', 'laranja', 'abacate', 'uva']
resultado = filtrar_strings_com_a(strings)
print("Strings que começam com 'a':", resultado)
print()

#2. Escreva uma função que receba uma lista de números como argumento e retorne o maior número da lista.
def encontrar_maior_numero(lista):
    return max(lista)
numeros = [3, 5, 2, 8, 1, 10, 4]
maior_numero = encontrar_maior_numero(numeros)
print("O maior número da lista é:", maior_numero)
print()

#3. Escreva uma função que recebe uma lista de números como parâmetro e retorna a soma total dos elementos 
# da lista
def somar_elementos(lista):
    return sum(lista)
numeros = [1, 2, 3, 4, 5]
soma = somar_elementos(numeros)
print(f"A soma total dos elementos da lista é: {soma}")
print()

#4. Escreva uma função que recebe uma lista de números como parâmetro e retorna o produto total dos elementos 
# da lista
def produto_elementos(lista):
    produto = 1
    for num in lista:
        produto *= num
    return produto
numeros = [1, 2, 3, 4]
produto = produto_elementos(numeros)
print(f"O produto total dos elementos da lista é: {produto}")
print()

#5. Escreva uma função que recebe uma lista de números como parâmetro e 
# retorna outra lista apenas com os números pares
def filtrar_pares(lista):
    return [num for num in lista if num % 2 == 0]
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = filtrar_pares(numeros)
print(f"Números pares da lista: {pares}")
print()

#6. Escreva uma função que recebe uma string como parâmetro e 
# retorna outra string onde substitui as vogais por x
def substituir_vogais_por_x(string):
    vogais = "aeiouAEIOU"
    resultado = ''
    for char in string:
        if char in vogais:
            resultado += 'x'
        else:
            resultado += char
    return resultado
entrada = input("Digite uma string: ")
string_modificada = substituir_vogais_por_x(entrada)
print(f"String com vogais substituídas por 'x': {string_modificada}")
print()

#7. Definir uma função que testa um caracter e retorna se é vogal ou não
def eh_vogal(caracter):
    vogais = "aeiouAEIOU"
    return caracter in vogais
caracter = input("Digite um caracter: ")
if eh_vogal(caracter):
    print(f"O caracter '{caracter}' é uma vogal.")
else:
    print(f"O caracter '{caracter}' não é uma vogal.")
print()

#8. Reescreva o exercício 6 usando a função reduce e a função definida no exercício anterior
from functools import reduce
def substituir_vogais_por_x_reduce(string):
    def substituir(char, resultado):
        if eh_vogal(char):
            return resultado + 'x'
        else:
            return resultado + char
    return reduce(lambda acc, char: substituir(char, acc), string, '')
entrada = input("Digite uma string: ")
string_modificada = substituir_vogais_por_x_reduce(entrada)
print(f"String com vogais substituídas por 'x' (usando reduce): {string_modificada}")
print()

#9. Crie uma função para percorrer uma string informando se o caracter é acentuado ou não
def verificar_acentuacao(string):
    acentuados = "áàãâéêíóôõúüÁÀÃÂÉÊÍÓÔÕÚÜ"
    for char in string:
        if char in acentuados:
            print(f"O caracter '{char}' é acentuado.")
        else:
            print(f"O caracter '{char}' não é acentuado.")
entrada = input("Digite uma string: ")
verificar_acentuacao(entrada)   
print()