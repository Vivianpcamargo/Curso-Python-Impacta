numero = int(input())
numeroPar = numero + 1
numeroImpar = numero - 1

for x in range(2):
    if numeroPar % 2 == 0:
        parPosterior = numeroPar
    else:
        numeroPar += 1

    if numeroImpar % 2 != 0:
        imparAnterior = numeroImpar
    else:
        numeroImpar -= 1

print(str(imparAnterior)+' '+str(parPosterior))

