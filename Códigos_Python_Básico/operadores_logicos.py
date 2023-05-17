numero_01 = int(input('Informe o primeiro número: '))
numero_02 = int(input('Informe o segundo número: '))

p = (numero_01 > numero_02)
q = (numero_01 != numero_02)
r = not(p or q) and (not p)
print('P = ', p)
print('Q = ', q)
print('R = ', r)
