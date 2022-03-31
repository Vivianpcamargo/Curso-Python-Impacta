qntdAlunos = int(input())

notaOriginal = {}
novaNota = {}
notaFinal = {}
exibiTexto = {}
qntdAlteradas = 0
i = 0
y = 0
useHifen = {}

while i < qntdAlunos:
    notaOriginal[i] = float(input())
    i = i + 1

while y < qntdAlunos:
    novaNota[y] = float(input())
    
    if notaOriginal[y] == 10.00:
        notaFinal[y] = notaOriginal[y]
        useHifen[y] = True
    elif novaNota[y] == 10.00:
        if (notaOriginal[y] + 2) >= 10.00:
            notaFinal[y] = 10.00
        else:
            notaFinal[y] = notaOriginal[y] + 2

        qntdAlteradas = qntdAlteradas + 1
        useHifen[y] = False
    else:
        notaFinal[y] = notaOriginal[y]
        useHifen[y] = True

    y = y + 1

print('NOTAS ALTERADAS: '+ str(qntdAlteradas))

for x in range(len(notaFinal)):
    if(100 <= x+1):
        indice = str(x+1)
    elif(10 <= x+1):
        indice = '0' + str(x+1)
    else:
        indice = '00' + str(x+1)

    if(10 <= notaOriginal[x]):
        notaOriginalString = str(format(notaOriginal[x], '.2f'))
    else:
        notaOriginalString = '0' + str(format(notaOriginal[x], '.2f'))

    if(10 <= notaFinal[x]):
        notaFinalString = str(format(notaFinal[x], '.2f'))
    else:
        notaFinalString = '0' + str(format(notaFinal[x], '.2f'))

    if (useHifen[x] == True):
        print('-('+indice+') original: '+notaOriginalString+' | final: '+notaFinalString)
    else:
        print('*('+indice+') original: '+notaOriginalString+' | final: '+notaFinalString)
