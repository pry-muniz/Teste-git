Dias_semana = {1:'domingo', 2:'segunda', 3:'terça', 4:'quarta', 5:'quinta', 6:'sexta', 7:'sábado'}
Numeros = int(input('Digite um número:'))
if Numeros in range(1,8):
    print('O dia da semana é:', Dias_semana[Numeros])
    