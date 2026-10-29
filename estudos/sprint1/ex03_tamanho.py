texto = input('Digite seu texto: ')

if len(texto) < 1000:
    print('O texto é curto')
elif len(texto) < 4000:
    print('O texto é médio')
else:
    print('O texto é longo')