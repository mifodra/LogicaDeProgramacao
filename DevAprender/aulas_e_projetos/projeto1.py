### Fatorial de um número ###
'''		
1. Um número
2. Multiplar o número por todos seus antecessores e depois exibir o resultado
3. Ter um número inteiro e positivo
4. Exibir em tela o fatorial do número inserido
5. - Pedir um número ao usuário
   - Multiplicar o número menos um até atingir o um (n * n-1)
   - Exibir em tela o resultado da multiplicação

Pseudocódigo:
    input numero
	if numero < 0
		print "digite apenar números positivos"
		input numero
	fatorial = numero
	while numero > 1
		fatorial = fatorial * (numero - 1)
		numero = numero - 1
	print fatorial
		
			OU
				
	input numero
	if numero < 0
		print "digite apenar números positivos"
		input numero
	fatorial = 1
	loop de 1 a numero
		fatorial = fatorial * numero
	print resultado
'''

numero = int(input('Digite um número: '))
if numero < 0:
    print('Digite apenas números positivos')
    numero = int(input('Digite um número: '))
fatorial = numero
while numero > 1:
    fatorial = fatorial * (numero - 1)
    numero = numero - 1
print(fatorial)

        # OU #

numero = int(input('Digite um número: '))
if numero < 0:
    print('Digite apenas números positivos')
    numero = int(input('Digite um número: '))
fatorial = 1
for item in range(1, numero + 1):
    fatorial = fatorial * item
print(fatorial)