# Verificar se um número é par ou ímpar sem usar o %.

print()
print('Informe um número para verificar se é par ou ímpar.')
print()

numero = float(input('Informe um número: '))

divisao = numero / 2
if divisao == int(divisao):
    print('O número {} é par.'.format(numero))
else:
    print('O número {} é ímpar.'.format(numero))
print()
print('Fim do programa.')
