### Medidor de Velocidade ###
'''
1. Velocidade
2. Comparar se a velocidade está menor ou igual, até 10km maior, entre 11km e 20km ou 20+km maior que 80km e exibir as mensagem referentes
3. -
4. Exibir em tela as mensagem referentes a cada velocidade atingida
5. - Pedir a velocidade ao usuário e guardar em uma variável
   - Comparar a velocidade com a velocidade permitida
   - Se o usuário estiver abaixo de 80km exibir: não houve multa
   - Se o usuário estiver entre 81km e 90km exibir: levou multa leve
   - Se o usuário estiver entre 91 e 100 exibir: levou multa grave
   - Se o usuário estiver acima de 101 exibir: levou multa gravíssima

Pseudocódigo:
	input velocidade
	velocidade_maxima = 80
	if velocidade <= velocidade_maxima
		print "não houve multa"
	if velocidade > velocidade_maxima e velocidade <= velocidade_maxima + 10
		print "levou multa leve"
	if velocidade > velocidade_maxima + 11 e velocidade <= velocidade_maxima + 20
		print "levou multa grave"
	else 
		print "levou multa gravíssima"
'''

velocidade = int(input('Digite sua velocidade: '))
velocidade_maxima = 80
if velocidade <= velocidade_maxima:
    print('não houve multa')
elif velocidade > velocidade_maxima and velocidade <= (velocidade_maxima + 10):
    print('levou multa leve')
elif velocidade >= (velocidade_maxima + 11) and velocidade <= (velocidade_maxima + 20):
    print('levou multa grave')
else:
    print('levou multa gravíssima')