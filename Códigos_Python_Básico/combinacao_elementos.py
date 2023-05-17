# Vamos considerar o problema de gerar as combinações de dois elementos a partir
# de um conjunto de números naturais com n elementos, ou seja, um conjunto
# A = {1, 2, 3, ..., n}. Antes de gerar as combinações, o código deve perguntar
# o número de elementos do conjunto ao usuário.

print()
print('***** Gerador de combinações de dois elementos *****')
print()

# solicita entra de dados
numero = int(input('Informe o número de elementos do conjunto: '))
# Imprime a saída dos dados com números sequenciados
print('Elementos do conjunto: ', end='')
# laço de repetição com o range de 1 até o número informado + 1. A variável cont recebe o valor de 1
for cont in range(1, numero + 1):
    print(cont, end=' ')  # imprime a saída dos dados com números sequenciados, ou seja, sem a quebra de linha
# escrevendo as combinações dos elementos
print('\nCombinações: ', end='')
# laços de repetição for aninhados, ou seja, um dentro do outro. O primeiro laço de repetição vai de 1 até o número informado + 1.
# A variável cont recebe o valor de 1.
# O segundo laço de repetição vai de 1 até o número informado + 1. A variável cont_2 recebe o valor de 1.
# O primeiro laço de repetição vai executar o segundo laço de repetição até que a condição seja falsa. Quando a condição for falsa,
# o primeiro laço de repetição vai executar o segundo laço de repetição novamente, mas com o valor da variável cont incrementado em 1.
for cont in range(1, numero + 1):
    for cont_2 in range(1, numero + 1):
        print('(', cont, ',', cont_2, ')', end=' ')
print()
print('Fim do programa.')

