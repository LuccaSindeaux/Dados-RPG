opcoes='''
    ========================
    0 - Encerrar programa
    1 - Dado de quatro lados
    2 - Dado de seis lados 
    3 - Dado de oito lados 
    4 - Dado de dez lados 
    5 - Dado de doze lados 
    6 - Dado de vinte lados
    7 - Dado de cem lados
    ======================== 
'''

import random

dado4=[]
dado6=[]
dado8=[]
dado10=[]
dado12=[]
dado20=[]
dado100=[]


def d4():
    numrol=int(input('Quantos D4 serão rolados? '))
    print(f'Rolando {numrol}D4...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,4)
        dado4.append(rol)
        rep+=1
    print(dado4)
    dado4.clear()

def d6():
    numrol=int(input('Quantos D6 serão rolados? '))
    print(f'Rolando {numrol}D6...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,6)
        dado6.append(rol)
        rep+=1
    print(dado6)
    dado6.clear()

def d8():
    numrol=int(input('Quantos D8 serão rolados? '))
    print(f'Rolando {numrol}D8...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,8)
        dado8.append(rol)
        rep+=1
    print(dado8)
    dado8.clear()

def d10():
    numrol=int(input('Quantos D10 serão rolados? '))
    print(f'Rolando {numrol}D10...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,10)
        dado10.append(rol)
        rep+=1
    print(dado10)
    dado10.clear()

def d12():
    numrol=int(input('Quantos D12 serão rolados? '))
    print(f'Rolando {numrol}D12...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,12)
        dado12.append(rol)
        rep+=1
    print(dado12)
    dado12.clear()

def d20():
    numrol=int(input('Quantos D20 serão rolados? '))
    print(f'Rolando {numrol}D20...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,20)
        dado20.append(rol)
        rep+=1
    print(dado20)
    dado20.clear()

def d100():
    numrol=int(input('Quantos D100 serão rolados? '))
    print(f'Rolando {numrol}D100...')
    rep=0
    while True:
        if rep == numrol:
            break
        rol=random.randint(1,100)
        dado100.append(rol)
        rep+=1
    print(dado100)
    dado100.clear()

while True:
    print(opcoes)
    escolha=int(input('Selecione uma opção: '))
    if escolha ==0:
        break
    if escolha == 1:
        d4()
    if escolha == 2:
        d6()
    if escolha == 3:
        d8()
    if escolha == 4:
        d10()
    if escolha == 5:
        d12()
    if escolha == 6:
        d20()
    if escolha == 7:
        d100()
    if escolha >=8 or escolha < 0:
        print('Número digitado não é uma das escolhas possíveis...')

#Só possível com a ajuda do Murilin <3

