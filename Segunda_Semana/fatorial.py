# Calcule o fatorial de um número.
# O fatorial de um número n, representado por n!, é calculado da seguinte forma:
# n! = n * (n-1) * (n-2) * ... * 1. Sendo que 1! = 0! = 1.

# Importando a biblioteca math
import math

print()
print('***** Fatorial *****')
print()
# Entrada de dados
numero = int(input('Infome um número: '))
# Utilizando a função factorial da biblioteca math
fatorial = math.factorial(numero)
print()
# Saída de dados
print('O fatorial de {} é {}'.format(numero, fatorial))

# Verificando o fatorial de um número utilizando o laço for

# Entrada de dados
numero = int(input('Infome um número: '))
fatorial = 1
for cont in range(numero, 1, -1):
    fatorial = fatorial * cont
    print()
    print(f'O fatorial de {numero} é {fatorial}')
