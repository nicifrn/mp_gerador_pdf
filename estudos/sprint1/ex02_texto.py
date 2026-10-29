texto = 'A menina aproximou-se da cama e sentiu um estranho calafrio ao olhar para a avó. Mudada e com as cobertas cobrindo quase todo o rosto, parecia outra pessoa. Tomando coragem, ela perguntou: — Ó, vovó, que orelhas tão grandes você tem… — É para te ouvir melhor, minha netinha.'

print('quantidade de caracteres: ', len(texto))
print('quantidade de palavras:', len(texto.replace('—', '').split()))
print('Texto com o travessão trocado por hífen: ', texto.replace('—', '-'))
print('Texto com as reticências trocadas por 3 pontos: ', texto.replace('…', '...'))