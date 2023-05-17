print('Informe dois números')

numero_1 = float(input('Informe o primeiro número: '))
print()
numero_2 = float(input('Informe o segundo número: '))
print()

operacao = input('Informe a operação a ser realizada (+, -, *, /): ')
if operacao == '+':
    soma = numero_1 + numero_2
    print('A soma dos números é: ', soma)
elif operacao == '-':
    subtracao = numero_1 - numero_2
    print('A subtração dos números é: ', subtracao)
elif operacao == '*':
    multiplicacao = numero_1 * numero_2
    print('A multiplicação dos números é: ', multiplicacao)
elif operacao == '/':
    divisao = numero_1 / numero_2
    print('A divisão dos números é: ', divisao)
else:
    print('Por favor, informe uma operação válida (+, -, *, /)')
