def classificar_tamanho(n):
    if len(n) < 1000:
        return('curto')
    elif len(n) < 4000:
        return('médio')
    else:
        return('longo')

for i in range(1, 4):
    texto = input(f'Digite o texto {i}: ')
    resultado = classificar_tamanho(texto)
    print(f'Resultado do texto {i}: {resultado}')