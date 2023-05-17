# O laço de repetição while precisa testar a condição de parada antes mesmo
# da primeira repetição. Entretanto, em diversos momentos, precisamos executar
# a primeira repetição antes a condição de parada.
# O código abaixo realiza a soma dos números informados peo usuário e encerra após
# a digitação do número 0 (zero).
print()
print('Informe os números para somar. Digite 0 (zero) para encerrar.')
print()
soma = 0
while True:
    numero = float(input('Informe um número: '))
    if numero == 0:
        break
    soma += numero
print('A soma dos números informados é: {}'.format(soma))

# O código abaixo realiza a soma dos números informados pelo usuário, porém,
# ao digitar números negativos, o programa ignora os mesmo e continua a execução.
# O programa só encerra após o usuário informar 0 (zero).

print()
print('Informe os números para somar. Números negativos serão ignorados. Digite 0 (zero) para encerrar.')
print()
soma = 0
while True:
    numero = float(input('Informe um número: '))
    if numero < 0:
        continue
    if numero == 0:
        break
    soma += numero
print('A soma dos números informados é: {}'.format(soma))

# O código abaixo realiza a soma dos números informados pelo usuário, porém,
# ele ignora os números ímpares. A soma dos números é encerrada após digitar 0 (zero).

print()
print('Informe os números para somar. Números ímpares serão ignorados. Digite 0 (zero) para encerrar.')
print()

soma = 0
while True:
    numero = float(input('Informe um número: '))
    if numero % 2 != 0:
        continue
    if numero == 0:
        break
    soma += numero
print('A soma dos números informados é: {}.'.format(soma))
