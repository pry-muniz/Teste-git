import random
numeros = []
quantidade_numeros = int(input('Digite a quantidade de numero que deseja: '))
while len(numeros) < quantidade_numeros:
    numeros.append(random.randrange(0,50))
print(numeros)
print('O maior valor dessa lista é: ', max(numeros))
print('O menor valor dessa lista é: ', min(numeros))