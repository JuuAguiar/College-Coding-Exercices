#Primeira Lista de Exercícios - Python


#1. Faça um programa que pergunte o nome, idade, peso e altura de uma pessoa e decide ser ela está apta
#a entrar no exercito.
#Obs: Para entrar no exercito é preciso ter mais de 18 anos, 
#pesar igual ou mais que 60 kg e medir mais ou igual que 1,70

print("Exercicio 1")
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))    
peso = float(input("Digite seu peso (kg): "))
altura = float(input("Digite sua altura (m): "))    
if idade > 18 and peso >= 60 and altura >= 1.70:
    print(f"{nome}, você está apto(a) a entrar no exército.")
else:
    print(f"{nome}, você não está apto(a) a entrar no exército.")
print()

print("Exercicio 2")
#2. Faça um programa que imprima a frase de tras para frente e veja o que está escrito. Palindromo - Anotaram a data da maratona

frase = "Anotaram a data da maratona"
frase_invertida = frase[::-1]
print(frase_invertida)
print()

print("Exercicio 3")
#3. Faça um programa que calcule quantos segundos tem:

#Entrada:
#dias = int(input("Dias: "))
#horas = int(input("Horas: "))
#minutos = int(input("Minutos: "))

dias = 2
horas = 3   
minutos = 5
segundos_totais = dias * 86400 + horas * 3600 + minutos * 60
print(f"O total de segundos em {dias} dias, {horas} horas e {minutos} minutos é: {segundos_totais} segundos.")
print()

print("Exercicio 4")
#4 Faça um programa que calcule o tempo de uma viagem de carro.
#Entrada:
#distância a percorrer e a velocidade média esperada para a viagem.

distancia = float(input("Digite a distância a percorrer (em km): "))
velocidade_media = float(input("Digite a velocidade média esperada (em km/h): "))
tempo_viagem = distancia / velocidade_media
print(f"O tempo estimado para a viagem é de {tempo_viagem:.2f} horas.")
print()

print("Exercicio 5")
#5. Faça um programa que recebe a velocidade do carro e, caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário foi multado.
#Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 80 km/h.

velocidade_carro = float(input("Digite a velocidade do carro (em km/h): "))
if velocidade_carro > 80:
    print("Você foi multado!")
    km_acima = velocidade_carro - 80
    multa = km_acima * 5
    print(f"O valor da multa é de R$ {multa:.2f}.")
else:
    print("Você não foi multado.")
print()

print("Exercicio 6")
#6. Faça um programa para aprovar o empréstimo bancário para compra de uma casa. 
# O programa deve perguntar o valor da casa a comprar, o salário e a quantidade de anos a pagar. 
# O valor da prestação mensal não pode ser superior a 30% do salário. 
# Calcule o valor da prestação como sendo o valor da casa a comprar dividido pelo número de meses a pagar.

valor_casa = float(input("Digite o valor da casa a comprar: R$ "))
salario = float(input("Digite o seu salário: R$ "))     
anos = int(input("Digite a quantidade de anos para pagar: "))
prestacao_mensal = valor_casa / (anos * 12)
if prestacao_mensal <= salario * 0.3:   
    print("Empréstimo aprovado!")
    print(f"O valor da prestação mensal será de R$ {prestacao_mensal:.2f}.")    
else:
    print("Empréstimo negado!")
    print(f"O valor da prestação mensal de R$ {prestacao_mensal:.2f} excede 30% do seu salário.")   
print()

print("Exercicio 7")

#7. Faça um programa para imprimir a tabuada (operação multiplicação) de um determinado número:

numero = int(input("Digite um número para ver a tabuada: "))
print(f"Tabuada do {numero}:")
for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} x {i} = {resultado}")
print()

print("Exercicio 8")
#8. Faça um programa que calcule o resto da divisão inteira entre dois números. 
# Utilize apenas as operações de soma e subtração para calcular o resultado.

dividendo = int(input("Digite o dividendo (número a ser dividido): "))
divisor = int(input("Digite o divisor (número pelo qual dividir): "))       
if divisor == 0:
    print("Erro: Divisão por zero não é permitida.")    
else:
    resto = dividendo
    while resto >= divisor:
        resto -= divisor
    print(f"O resto da divisão inteira entre {dividendo} e {divisor} é: {resto}")   
print()

print("Exercicio 9")
#Escreva um programa que leia 3 números inteiros referentes ao comprimento dos lados de um triângulo 
# e classifique-o como: triângulo equilátero, isósceles ou escaleno.

lado1 = int(input("Digite o comprimento do primeiro lado do triângulo: "))
lado2 = int(input("Digite o comprimento do segundo lado do triângulo: "))
lado3 = int(input("Digite o comprimento do terceiro lado do triângulo: "))
if lado1 == lado2 == lado3:
    print("O triângulo é equilátero.")  
elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
    print("O triângulo é isósceles.")   
else:
    print("O triângulo é escaleno.")
print()

print("Exercicio 10")
#10. Escreva uma função que receba um número inteiro como entrada (px.: 32243) 
# e retorne o número invertido (px.: 34223).

def inverter_numero(numero):
    numero_invertido = 0
    while numero > 0:
        digito = numero % 10
        numero_invertido = numero_invertido * 10 + digito
        numero //= 10
    return numero_invertido

numero = int(input("Digite um número inteiro: "))
print(f"O número invertido é: {inverter_numero(numero)}")
print()

print("Exercicio 11")
# Escreva uma função que receba uma string e conte o número de vogais dentro dela, por exemplo:
# Entrada: 'Ciência de Dados'
# Saida: 'A palavra tem 7 vogais'

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

print("Exercicio 12")
#Escreva um programa que encontre o item mais frequente de uma lista. 
# Exemplo: [2, 7, 7, 7, '#', '#', '#', '@', 3, '#', 6]
# Saída: O caractere mais frequente é '#' e aparece 4 vezes

def item_mais_frequente(lista):
    frequencia = {}
    for item in lista:
        if item in frequencia:
            frequencia[item] += 1
        else:
            frequencia[item] = 1
    item_frequente = max(frequencia, key=frequencia.get) # type: ignore
    return item_frequente, frequencia[item_frequente]       
lista = [2, 7, 7, 7, '#', '#', '#', '@', 3, '#', 6]
item, vezes = item_mais_frequente(lista)    
print(f"O caractere mais frequente é '{item}' e aparece {vezes} vezes.")
print()

print("Exercicio 13")
#Escreva um programa para verificar se uma palavra é ou não um palíndromo.
#Ex:
#Digite uma palavra: ovo
#ovo é um palindromo 

def verificar_palindromo(palavra):
    palavra_invertida = palavra[::-1]
    return palavra == palavra_invertida
palavra = input("Digite uma palavra: ")
if verificar_palindromo(palavra):
    print(f"{palavra} é um palíndromo.")
else:
    print(f"{palavra} não é um palíndromo.")
print()


