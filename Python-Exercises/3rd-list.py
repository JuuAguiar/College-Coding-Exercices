#Terceira Lista de Exercícios - Python
#Strings e Bibliotecas

#1. Desenha moldura. Construa uma função que desenhe um retângulo usando os caracteres '+' , '−' e '| '. 
# Esta função deve receber dois parâmetros, linhas e colunas, sendo que o valor por omissão é o valor mínimo igual 
# a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa de forma elegante.
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

#2. Escreva uma função que receba uma string e uma lista. A função deve comparar a string passada
#com os elementos da lista, também passada como parâmetro. Retorne verdadeiro se a string for encontrada dentro da lista, e falso, caso contrário.
def verificar_string_na_lista(string, lista):
    return string in lista
entrada = input("Digite uma string: ")
lista = ['maçã', 'banana', 'laranja', 'uva']
encontrada = verificar_string_na_lista(entrada, lista)
print(f"A string '{entrada}' está na lista: {encontrada}")
print()

#3. Crie um programa que transfome o real em dólar
dolar = float(input("Digite o valor em reais: R$ "))
cotacao = float(input("Digite a cotação do dólar: R$ "))
valor_dolar = dolar / cotacao
print(f"O valor em dólares é: $ {valor_dolar:.2f}")
print()

#4. Crie um programa que calcule 25% de aumento no salário
salario = float(input("Digite o salário atual: R$ "))
aumento = salario * 0.25
novo_salario = salario + aumento
print(f"O novo salário com 25% de aumento é: R$ {novo_salario:.2f}")
print()

#5. Crie um programa que transfome a letra Maiuscula em Minuscula
letra_maiuscula = input("Digite uma letra maiúscula: ")
letra_minuscula = letra_maiuscula.lower()
print(f"A letra minúscula é: {letra_minuscula}")
print()

#6. Crie um programa que verifica se a pessoa está apta ou não para votar nas eleições.
#Critérios:
#Idade menor que 16: Não pode votar
#16 <= Idade < 18: Opcional
#18 <=Idade <= 65: Obrigatório
#Idade maior que 65: Opcional
idade = int(input("Digite sua idade: "))
if idade < 16:
    print("Não pode votar.")
elif 16 <= idade < 18 or idade > 65:
    print("Voto opcional.")
else:
    print("Voto obrigatório.")
print()

#7. Crie um programa que leia o seu nome completo e que apresente somente o seu primeiro e último nomes
nome_completo = input("Digite seu nome completo: ")
partes_nome = nome_completo.split()
primeiro_nome = partes_nome[0]
ultimo_nome = partes_nome[-1]
print(f"Primeiro nome: {primeiro_nome}")
print(f"Último nome: {ultimo_nome}")
print()

#8. Crie um programa que leia um número qualquer e informe se ele é par ou ímpar
numero = int(input("Digite um número: "))
if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
print()

#9. Crie um programa que apresente o maior e o menor valores da sequência ([54, 10, 29, 87, 7, 64]
sequencia = [54, 10, 29, 87, 7, 64]
maior = max(sequencia)
menor = min(sequencia)
print(f"O maior valor da sequência é: {maior}")
print(f"O menor valor da sequência é: {menor}")
print()
