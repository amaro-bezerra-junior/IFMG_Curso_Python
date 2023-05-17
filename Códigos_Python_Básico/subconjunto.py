# Subconjuntos

# Vamos considerar o problema de gerar os subconjuntos de dois elementos a partir
# de um conjunto com n elementos naturais.
# Pela definição matemática, temos que considerar os seguintes pontos:
# 1. Os subconjuntos não podem ter elementos repetidos;
# 2. A ordem dos elementos não importa e não altera o conjunto;
# 3. Não devemos ter subconjuntos repetidos.

print()
print('***** Subconjuntos *****')
print()

numero = int(input('Informe o número de elementos do conjunto: '))
print()
print('Elementos: ', end= '')
for cont in range(1, numero + 1):
    print(cont, end= ' ')
print()
print('\nSubconjuntos: ', end = ' ')
for cont_1 in range(1, numero + 1):
    for cont_2 in range(cont_1 + 1, numero + 1):
        print('{', cont_1, ',', cont_2, '}', sep= '', end= '')
print()
print('Fim do programa.')
