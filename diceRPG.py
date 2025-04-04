from random import randint

opcoes2 = '''
    ============================================
    0 - Encerrar programa
    1 - Dado de quatro lados
    2 - Dado de seis lados 
    3 - Dado de oito lados 
    4 - Dado de dez lados 
    5 - Dado de doze lados 
    6 - Dado de vinte lados
    7 - Dado de cem lados (1,100)
    8 - Dado de cem lados (10,100 de 10 em 10)
    =============================================
'''

alt100 = [valor*10 for valor in range(1, 11)]


def rolar_dado(lados):
    numrol = int(input(f'Quantos D{lados} serão rolados? '))
    print(f'Rolando {numrol}D{lados}...')
    rolagens = [randint(1, lados) for _ in range(numrol)]
    print(rolagens)

opcoes = {
    1: 4,
    2: 6,
    3: 8,
    4: 10,
    5: 12,
    6: 20,
    7: 100,
    8: alt100,
}

while True:
    print(opcoes2)
    escolha = int(input('Selecione uma opção: '))
    
    if escolha == 0:
        break

    if escolha == 8:
        print(opcoes.get(escolha))
        continue
    
    lados = opcoes.get(escolha)
    if lados:
        rolar_dado(lados)
    else:
        print('Número digitado não é uma das escolhas possíveis...')
