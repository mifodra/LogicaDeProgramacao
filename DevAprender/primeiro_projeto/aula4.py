### Coleções (listas)
preço_1 = 20
preço_2 = 50
preço_3 = 200
# Lista
precos = [20, 50, 200]
#         0,   1,  2
print(precos[1]) #50
print(precos.index(200)) #2

diversidades = [15, 'Jhonatan', True]
print(diversidades[0])
print(diversidades[1])
print(diversidades[2])
# Laços em iteráveis
for diversidade in diversidades:
    print(diversidade)

'''
Soma de valores de uma lista [15, 46, 75, 34, 23]
'''
idades = [15, 46, 75, 34, 23]
total = 0
for idade in idades:
    total = total + idade
print(total)