### Chute um número ###
'''
1. - Um número de 0 a 10
   - Um chute do usuário
2. - Comparar o número inserido com o número gerado pelo programa
   - Se o valor for diferente do esperado: exibir se o número é maior ou menor que o esperado e permitir a inserção de outro valor
3. - O usuário pode chutar até acertar o valor
   - O usuário pode jogar quantas vezes quiser
4. Que o usuário acerte o número gerado pelo programa
5. - Gerar um número aleatório de 0 a 10
   - Guardar o número aleatório
   - Perguntar um valor ao usuário
   - Comparar o valor do usuário com o valor gerado pelo programa
   - Se o usuário acertar o número: exibir uma mensagem parabenizando
   - Se o usuário errar o número: exibir se o número é maior ou menor que o esperado e permitir a inserção de outro valor

Pseudocódigo:
	valor_aleatorio
	input chute
	while chute != valor_aleatorio
		if chute > valor_aleatorio
			print "chute é maior que o valor gerado"
		else
			print "chute é menor que o valor gerado"
		input chute
	print "acertou o chute"
				
			OU
		
	valor_aleatorio
	acertou = falso
	while acertou = falso
		input chute
		if chute > valor_aleatorio
			print "chute é maior que o valor gerado"
		if chute < valor_aleatorio
			print "chute é menor que o valor gerado"
		if chute = valor_aleatorio
			print "acertou o chute"
			acertou = verdadeiro
		else
			print "você chutou um valor inválido"
'''
import random

valor_aleatorio = random.randint(1,10)
chute = int(input('Chute um valor de 1 a 10'))
while chute != valor_aleatorio:
    if chute > valor_aleatorio:
        print('chute é maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('chute é menor que o valor gerado')
    chute = int(input('Digite seu chute: '))
print('Acertou o chute')

        # OU #

valor_aleatorio = random.randint(1,10)
acertou = False
while acertou == False:
    chute = int(input('Chute um valor de 1 a 10'))
    if chute > valor_aleatorio:
        print ('chute é maior que o valor gerado')
    elif chute < valor_aleatorio:
        print('chute é menor que o valor gerado')
    elif chute == valor_aleatorio:
        print('acertou o chute')
        acertou = True
    else:
        print('você chutou um valor inválido')
