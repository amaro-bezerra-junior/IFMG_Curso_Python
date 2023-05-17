# O laço de repetição for é utilizado quando sabemos a quantidade de repetições.
# O laço de repetição for é composto por 3 partes:
# 1. Inicialização: onde definimos o valor inicial da variável de controle.
# 2. Condição: onde definimos a condição que deve ser verdadeira para que o
#    laço continue executando.
# 3. Incremento: onde definimos o valor que será adicionado à variável de
#    controle a cada repetição.
# Vamos considerar o problema para somar 10 números informados pelo usuário.

soma = 0  # variável de controle
for cont in range(10):  # condição
    numero = float(input('Informe o {}º número: '.format(cont + 1)))
    soma += numero  # incremento
print('A soma dos números informados é', soma)

# É possível notar no códido acima, que a única função da variável count é
# controlar as repetições do laço. Quando temos uma variável que não é usada em
# nenhuma outra parte do código, podemos substituí-la por um underline (_).

# Outro detalhe importante é a função range(). Além do fim do intervalo, podemos
# definir o início e a periodicidade dos números. Por exemplo, a instrução
# range(2, 6), será retomado o intervalo "2, 3, 4 e 5", ou seja, o primeiro
# número é o início do intervalo e o segundo é o fim. Lembrando que o número fim
# nesse caso o número "6", não é incluído no intervalo.

soma = 0
for cont in range(2, 6):
    numero = float(input('Informe o {}º número: '.format(cont)))
    soma += numero
print('A soma dos números informados é', soma)

# Quando incluímos um terceiro número na função range(), definimos a periodicidade
# dos números. Como exemplo, se usarmos a instrução range(3, 19, 4) teremos a
# sequência "3, 7, 11, 15". A sequência começa em 3, e os demais são obtidos
# somando 4 ao número atual, até atingir o fim do intervalo, neste caso,
# o número 19..

soma = 0
for cont in range(3, 19, 4):
    numero = float(input('Informe o {}º número: '.format(cont)))
    soma += numero
print('A soma dos números informados é', soma)

# Além disso, no lugar dos números, podemos usar qualquer variável ou expressão
# que retorne um número inteiro. Também podemos obter intervalos em ordem
# decrescente, por exemplo, a instrução range(5, 0, -1) retornará a sequência
# 5, 4, 3, 2, 1.

soma = 0
for cont in range(5, 0, -1):
    numero = float(input('Informe o {}º número: '.format(cont)))
    soma += numero
print('A soma dos números informados é', soma)
