contos = ['chapeuzinho vermelho', 'os 3 porquinhos', 'a raposa e as uvas', 'cinderela', 'branca de neve']

for indice, lista in enumerate(contos, start=1):
    print(f'{indice}. {lista}')

total = len(contos)
print(f'\nO total de contos na lista é: {total}')