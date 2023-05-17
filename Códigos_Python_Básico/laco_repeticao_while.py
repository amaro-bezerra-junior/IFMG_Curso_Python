# Programa que recebe um número e imprime todos os números pares iniciando de 0
# e encerrando no número informado pelo usuário.
# Caso o usuário informe o número 0, o programa não imprime nada.
# O laço de repetição while é utilizado quando não sabemos a quantidade de
# repetições que o programa deve executar.

atual = 0
numero = float(input('Informe um número: '))
while atual < numero:
    print(atual)
    atual += 2
