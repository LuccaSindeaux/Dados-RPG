import random

d100=[10,20,30,40,50,60,70,80,90,100]
list_dice=[]

menu='''
=======================================================
            'ROLAGENM DE DADOS DE RPG: 
    ATENÇÃO: digitar o número 0 encerrará o rpograma
=======================================================
'''

choice_100='''
Qual é o estilo de D100 que será rolado: 
1 - D100 de 1 a 100.
2 - D100 de 10 a 100 pulando de 10 em 10.
'''

def dado():
    numrol=int(input(f'Quantos D{escolha} serão rolados? '))
    print(f'Rolando {numrol} D{escolha} lados...')
    rep=0
    while True:
        if rep==numrol:
            break
        rol=random.randint(1,escolha)
        list_dice.append(rol)
        rep+=1
    print(list_dice)
    list_dice.clear()

def d_100():
    print(choice_100)
    option=int(input('Digite sua escolha: '))
    if option ==1:
        numrol=int(input(f'Quantos D{escolha} serão rolados? '))
        print(f'Rolando {numrol} D{escolha} lados...')
        rep=0
        while True:
            if rep==numrol:
                break
            rol=random.randint(1,escolha)
            list_dice.append(rol)
            rep+=1
        print(list_dice)
        list_dice.clear()

    if option ==2:
        numrol=int(input(f'Quantos D{escolha} serão rolados? '))
        print(f'Rolando {numrol} D{escolha} lados...')
        rep=0
        while True:
            if rep==numrol:
                break
            rol=random.choice(d100)
            list_dice.append(rol)
            rep+=1
        print(list_dice)
        list_dice.clear()

    if option not in (1,2):
        print('Favor selecionar 1 ou 2...')



while True:
    print(menu)
    escolha=int(input('Digite o dado que será rolado: '))
    if escolha==0:
        break
    if escolha not in (0,4,6,8,10,12,20,100):
        print('Dado não existe....')
    if escolha in (4,6,8,10,12,20):
        dado()
    if escolha==100:
        d_100()