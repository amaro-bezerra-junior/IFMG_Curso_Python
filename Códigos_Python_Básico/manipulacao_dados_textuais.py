nome_completo = input('Informe o seu nome completo: ')
sobrenome = input('Informe o seu sobrenome: ')

pos = nome_completo.find(sobrenome)
if pos != -1:
    print('Seu sobrenome começas na posição', pos)
else:
    print('Sobrenome não encontrado')

n = float(input('Informe um número: '))
print('{n:8f}'.format(n=n))
