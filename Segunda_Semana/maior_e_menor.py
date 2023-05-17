# Leia uma quantidade indeterminada de números. A cada número informado, o usuário
# deve informar se deseja continuar ou parar. Ao final, o código deve retornar
# o maior e o menor número recebido.

print()
print('***** Programa informa o menor e o maior número digitado *****')
print()

maior = float('-inf') # -inf é o maior número possível
menor = float('inf') # inf é o menor número possível

while True:
    numero = float(input('Digite um número: ')) # entrada dos dados
    if numero > maior: # comparação dos dados
        maior = numero # atribuição dos dados
    if numero < menor: # comparação dos dados
        menor = numero # atribuição dos dados
    opcao = str(input('Deseja continuar [S/N]: ')) # entrada dos dados
    if opcao.lower() == 'n': # comparação dos dados
        break # interrupção do laço
# saída dos dados
print('O menor número digitado foi: ', menor)
print('O maior número digitado foi: ', maior)
print('Fim do programa.')
 