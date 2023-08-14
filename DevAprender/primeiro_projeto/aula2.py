### Condicionais (if, elif e else) ###
'''
E ae, boa dar uma saída hoje?
Se eu terminar meu trabalho aqui, eu consigo.
'''
trabalho_terminado = False
if trabalho_terminado == True:
    print('Opa! Bora dar uma saída.')
else:
    print('Não posso sair agora.')


'''
Ei, você consegue me ajudar a moves essas caixar lá pra fora hoje a tarde?
Se eu estiver livre, sim. Mas se não der pede para o meu irmão te ajudar.
'''
estou_livre = True
if estou_livre == True:
    print('Ok, posso ajudar hoje sim!')
else:
    print('Peça ao meu irmão para te ajudar.')


'''
Cheguei atrasado na aula, ainda posso entrar?
Se essa não for sua terceira vez chegando atrasado, então pode sim, caso contrário irá tomar uma susprensão.
'''
numero_de_atrasos = 0
if numero_de_atrasos >= 3:
    print('Você está suspenso')
elif numero_de_atrasos == 1:
    print('Pode entrar, porém caso tome mais 2 faltas, irá ser suspenso')
elif numero_de_atrasos == 2:
    print('Pode entrar, porém caso tome mais 1 falta, irá ser suspenso')
else:
    print('Pode entrar')


'''
Encontre o maior entre 2 números
'''
primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')
if primeiro_valor > segundo_valor:
    print('O primeiro valor é maior!')
elif primeiro_valor < segundo_valor:
    print('O segundo valor é maior!')
else:
    print('Os valores são iguais')