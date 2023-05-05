# Escreva um código que receba um número em segundos e converta para horas,
# minutos e segundos. Escreva também um código que faça o contrário.
print()
print('***** Conversor de segundos para horas, minutos e segundos *****')
print()

opcao = int(input('Digite 1 para converter segundos para horas, minutos e segundos ou 2 para converter horas, minutos e segundos para segundos: '))

if opcao == 1:
    segundos = int(input('Digite o número de segundos: '))
    conversor_minutos = segundos // 60
    conversor_segundos = segundos % 60
    conversor_hora = conversor_minutos // 60
    print('Os segundos informados equivalem a: ', conversor_hora, 'hora(s)',
          conversor_minutos, 'minuto(s) e', conversor_segundos, 'segundo(s)')
elif opcao == 2:
    horas = int(input('Digite o número de horas: '))
    minutos = int(input('Informe os minutos: '))
    segundos = int(input('Informe os segundos: '))
    total_segundos = (horas * 3600) + (minutos * 60) + segundos
    print('O valor total de segundos é: ', total_segundos, 'segundos')
