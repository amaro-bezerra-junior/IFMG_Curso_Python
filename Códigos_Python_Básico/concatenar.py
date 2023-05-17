""" O operador + pode ser usado para concatenar variáveis e literais textuais.
No entanto, não é possível concatenar diretamente um elemento textual e um elemento
numérico. Nesse caso, é necessário converter o valor numérico para textual antes
da concatenação."""

print('Informe os dados')
print()

nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
idade = int(input('Informe a idade: '))

mensagem = (nome + ' ' + sobrenome + ' tem ' + str(idade) + ' anos.')
print(mensagem)
