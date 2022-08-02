#>>>>>CALCULADORA DE VELOCIDADE MÉDIA<<<<<
#>>>>>ENTRADAS DE DISTANCIA E TEMPO<<<<<
distancia = input("DIGITE A DISTÂNCIA PERORRIDA: ")
tempo = input("DIGITE O TEMPO EM HORAS PARA PERCORRER A DISTÂNCIA: ")
#>>>>>CALCULO<<<<<
velocidade_media = float(distancia) / float(tempo)
#>>>>>IMPRESSÃO DO RESULTADO<<<<<
print("A VELOCIDADE MÉDIA FOI DE {:.2f}KM/h".format(velocidade_media))