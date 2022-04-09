diaSemana = input()
qntDias = int(input())

if diaSemana == 'domingo':
    contagem = 1
elif diaSemana == 'segunda':
    contagem = 2
elif diaSemana == 'terca':
    contagem = 3
elif diaSemana == 'quarta':
    contagem = 4
elif diaSemana == 'quinta':
    contagem = 5
elif diaSemana == 'sexta':
    contagem = 6
elif diaSemana == 'sabado':
    contagem = 7

calculo = contagem + qntDias

if calculo > 7:
    numeroDia = calculo - 7
else:
    numeroDia = calculo


if qntDias == 0:
    print('chega hoje!')
elif numeroDia == 1:
    print('sera entregue domingo')
elif numeroDia == 2:
    print('sera entregue segunda')
elif numeroDia == 3:
    print('sera entregue terca')
elif numeroDia == 4:
    print('sera entregue quarta')
elif numeroDia == 5:
    print('sera entregue quinta')
elif numeroDia == 6:
    print('sera entregue sexta')
elif numeroDia == 7:
    print('sera entregue sabado')
