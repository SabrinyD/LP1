tamanho = float (input('Informe o tamanho do arquivo para download (MG): '))
velocidade = float(input('Informe a velocidade do link de internet (Mbps): '))

velocidade_mbps = velocidade / 8
tempo_segundos = tamanho / velocidade_mbps
tempo_minutos = tempo_segundos / 60

print('O tempo aproximado para download é de {} minutos'.format(tempo_minutos))