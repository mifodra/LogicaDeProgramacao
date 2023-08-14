### Laços de Repetição + Listas

## For
'''
for item in coleção:
    expressão
'''
# range(início, fim, pulo)
for palavra in range (1,4):
    print('Carregando')

for item in range(1,20):
    print(item)

for item in range(1,20,2):
    print(item)

# listas = []
nomes = ['Jhonatan', 'Cristian', 'Roberto', 'Camila']
for nome in nomes:
    print(nome)

'''
De 1 a N
'''
numero_maximo = int(input('Digite o valor máximo: '))
for numero in range (1, numero_maximo + 1):
    print(numero)