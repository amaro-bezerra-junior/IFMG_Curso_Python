# Receber três números e informar o mairo deles.

print()
print('Verifica qual dos três números é o maior.')
print()

numero_1 = float(input('Informe o primeiro número: '))
numero_2 = float(input('Informe o segundo número: '))
numero_3 = float(input('Informe o terceiro número: '))

if numero_1 == numero_2 and numero_2 == numero_3:
    print('Os três números são iguais.')
elif numero_1 > numero_2 and numero_1 > numero_3:
    print('O número {} é o maior.'.format(numero_1))
elif numero_2 > numero_1 and numero_2 > numero_3:
    print('O número {} é o maior.'.format(numero_2))
elif numero_3 > numero_1 and numero_3 > numero_2:
    print('O número {} é o maior.'.format(numero_3))
elif numero_1 == numero_2 and numero_1 > numero_3:
    print('Os números {} e {} são os maiores.'.format(numero_1, numero_2))
elif numero_1 == numero_3 and numero_1 > numero_2:
    print('Os números {} e {} são os maiores.'.format(numero_1, numero_3))
elif numero_2 == numero_3 and numero_2 > numero_1:
    print('Os números {} e {} são os maiores.'.format(numero_2, numero_3))
else:
    print('Os números {} e {} são os maiores.'.format(numero_1, numero_2))
print()
print('Fim do programa.')
