# Simular uma calculadora simples. O código deve solicitar ao usuário a operação
# desejada (soma, subtração, multiplicação, divisão ou potência) ou então sair.
# Quando o usuário escolher uma operação, o código deve solicitar dois números,
# realizar a operação e exibir o resultado. O código deve sempre solicitar uma nova
# operação até que o usuário escolha sair.

print()
print('***** Calculadora Simples - Realiza a operação de dois valores *****')
print()

while True:
    operacao = str(
        input('Informe a operação desejada [+, -, *, /, ** ou S para sair]: ')).lower()
    print()
    if operacao.lower() == 's':
        break
    numero_1 = float(input('Informe o primeiro número: '))
    numero_2 = float(input('Informe o segundo número: '))
    print()
    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    elif operacao == '**':
        resultado = numero_1 ** numero_2
    elif operacao == '/':
        if numero_2 == 0:
            print('Não é possível dividir por zero.')
            continue
        resultado = numero_1 / numero_2
    print(numero_1, operacao, numero_2, '=', resultado)
