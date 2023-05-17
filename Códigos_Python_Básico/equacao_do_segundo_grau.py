import math

# Ax² + Bx + C = 0

print('***** Equação do Segundo Grau *****')
print()
print('*** Informe os valores de A, B e C para calcular o valor de X ***')
print()

a = float(input('Digite o valor de A: '))
b = float(input('Digite o valor de B: '))
c = float(input('Digite o valor de C: '))

if a == 0:
    print('Não é uma equação do segundo grau.')
else:
    delta = b ** 2 - 4 * a * c
    if delta < 0:
        print('A equação não possui raízes reais.')
    elif delta == 0:
        x_1 = b * (-1) / (2 * a)
        print('A equação possui apenas uma raiz real: ', x_1)
    else:
        raiz_delta = math.sqrt(delta)
        x_1 = (b * (-1) + raiz_delta) / (2 * a)
        x_2 = (b * (-1) - raiz_delta) / (2 * a)
        print('A equação possui duas raízes reais: ', x_1, ' e ', x_2)
