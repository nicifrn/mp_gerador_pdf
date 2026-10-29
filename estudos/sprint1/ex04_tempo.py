import time

inicio = time.perf_counter()
soma = 0

for numeros in range(1,1000001):
    soma += numeros

fim = time.perf_counter()
tempoms = (fim - inicio ) * 1000

print(f'Resultado da soma: {soma}')
print(f'Tempo para somar: {tempoms:.2f} ms')
