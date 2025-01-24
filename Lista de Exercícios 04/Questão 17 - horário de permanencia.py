horario_entrada = int(input('Informe o horário de entrada: '))
minuto_entrada = int(input('Informe o minuto de entrada: '))
horario_saida = int(input('Informe o horário de saída: '))
minuto_saida = int(input('Informe o minuto de saída: '))

entrada_completa = horario_entrada * 60 + minuto_entrada
saida_completa = horario_saida * 60 + minuto_saida
permanencia_completa = saida_completa - entrada_completa
hora_permanencia = permanencia_completa // 60
minuto_permanencia = permanencia_completa % 60


print("O tempo de permanência foi:", hora_permanencia, "h", minuto_permanencia, "m")