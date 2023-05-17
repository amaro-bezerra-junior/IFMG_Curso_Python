# Cálculo MDC - Máximo Divisor Comum

# Um problema interessante para ser resolvido com o laço de repetição é o cáclulo
# máximo divisor comum, ou MDC, de dois números inteiros com a técnica de Euclides.
# Lembrando que o MDC de números é o maior número que os divide sem deixar restos.
# Basicamente, a técnica de Euclides consiste nos seguintes passos:
# 1. Dividimos o maior número pelo menor número e verificamos se o resto da
# divisão é zero.
# 2. Em caso afirmativo, o menor número é o MDC.
# 3. Caso contrário, substituímos o maior pelo menor, o menor número pelo resto
# da divisão e repetimos o processo a partir do passo 1.
# O código abaixo implementa a técnica de Euclides para calcular o MDC de dois
# números inteiros. São eles 144 por 56.

print()
print('MDC - Máximo Divisor Comum - números inteiros')
print()

print('***** Informe dois números inteiros *****')
print()

numero_01 = int(input('Informe o primeiro número: '))
numero_02 = int(input('Informe o segundo número: '))

if numero_01 < 1 or numero_02 < 1:
    print('Números invalidos para verificar o MDC!')
else:
    while True:
        resto = numero_01 % numero_02
        print(numero_01, '/', numero_02, 'tem resto: ', resto)
        if resto == 0:
            break
        numero_01 = numero_02
        numero_02 = resto
    print('O MDC é: ', numero_02)
