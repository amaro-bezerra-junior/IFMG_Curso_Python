# Calcular o imposto de renda de um sálario considerando as seguintes
# alíquotas:

# Até R$ 1.903,98 isento;
# De R$ 1.903,99 até R$ 2.826,65 7,5%;
# De R$ 2.826,66 até R$ 3.751,05 15%;
# De R$ 3.751,06 até R$ 4.664,68 22,5%;
# Acima de R$ 4.664,68 27,5%.

print()
print('***** Verificar o imposto de renda *****')
print()

salario = float(input('Informe o salário: '))

if salario <= 1903.98:
    print('Isento de imposto de renda.')
elif salario >= 1903.99 and salario <= 2826.65:
    imposto = (salario * 0.075)
    print('O valor do imposto de renda é de R$ {:.2f}.'.format(imposto))
elif salario >= 2826.66 and salario <= 3751.05:
    imposto = (salario * 0.15)
    print('O valor do imposto de renda é de R$ {:.2f}.'.format(imposto))
elif salario >= 3751.06 and salario <= 4664.68:
    imposto = (salario * 0.225)
    print('O valor do imposto de renda é de R$ {:.2f}.'.format(imposto))
else:
    imposto = (salario * 0.275)
    print('O valor do imposto de renda é de R$ {:.2f}.'.format(imposto))
print()
print('Fim do Programa.')
