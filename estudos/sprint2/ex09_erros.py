try:
    with open("nao_existe.txt", "r", encoding="utf-8") as f:
        conteudo = f.read()
        print(conteudo)

except FileNotFoundError:
    print("Erro: O ficheiro 'nao_existe.txt' não foi encontrado. Verifique o nome e tente novamente.")