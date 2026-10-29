arquivo = "/home/bruno/mp_gerador_pdf_estudos/estudos/sprint2/narrativa_teste.txt"

with open(arquivo, 'r') as f:
    conteudo = f.read()

parte = conteudo.split('---', 1)
cabecalho = parte[0]
texto = parte[1].strip().replace('\n', ' ') # Coloquei isso para não aparecer os \n no resultado

narrativa = {}
linhas_cabecalho = cabecalho.split('\n')

for linha in linhas_cabecalho:
    if ':' in linha:
        rotulo, valor = linha.split(':', 1)
        narrativa[rotulo.strip()] = valor.strip()

narrativa['texto'] = texto

print('Dicionario:\n', narrativa)
print(f'\ntitulo: {narrativa['titulo']}')
print(f'Quantidade de caracteres do texto: {len(narrativa['texto'])}')