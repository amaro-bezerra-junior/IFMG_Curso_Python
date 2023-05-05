# Considere a fórmula para calcular juros simples: J = (C * I * T),
# onde J, C, I e T correspondem a juros, capital, taxa e tempo, respectivamente.
# Escreva um código que solicite ao usuário os valores de C, I e T
# e calcule o valor de J.
print()
print('***** Calculadora de juros simples *****')
print()

capital = float(input('Informe o valor do capital: '))
taxa = float(input('Informe o valor da taxa: '))
opcao = float(
    input('Informe 1 para o período em meses e 2 para o período em anos: '))

if opcao == 1:
    tempo = float(input('Informe o valor do tempo em meses: '))
    juros = (capital * taxa * tempo) / 100
    print()
    print('O valor correspondente ao juros é: R$', juros)

elif opcao == 2:
    tempo = float(input('Informe o valor do tempo em anos: '))
    periodo = tempo * 12
    juros = (capital * taxa * periodo) / 100
    print()
    print('O valor correspondente ao juros é: R$', juros)
