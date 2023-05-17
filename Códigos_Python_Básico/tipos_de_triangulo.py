print('***** Informe os lados de um triângulo *****')
print()

a = float(input('Informe o lado A: '))
b = float(input('Informe o lado B: '))
c = float(input('Informe o lado C: '))

if (a > b + c) or (b > a + c) or (c > a + b):
    print('Não é um triângulo')
elif (a == b) and (b == c):
    print('Triaângulo equilátero.')
elif (a == b) or (b == c) or (a == c):
    print('Triângulo isósceles.')
else:
    print('Triângulo escaleno.')

