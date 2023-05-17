# Verifica se as notas do aluno e calcula a média informando se o aluno foi aprovado ou não

nota_01 = float(input('Informe a primeira nota do aluno: '))
nota_02 = float(input('Informe a segunda nota do aluno: '))

media = (nota_01 + nota_02) / 2

if media >= 7:
    print('O Aluno obteve média {:.2f} e foi APROVADO!'.format(media))
elif media >= 5 and media < 7:
    print('O Aluno obteve média {:.2f} e está de RECUPERAÇÃO!'.format(media))
else:
    print('O Aluno obteve média {:.2f} e foi REPROVADO!'.format(media))
