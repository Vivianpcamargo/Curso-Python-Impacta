inicio = int(input())
fim = int(input())

numero = inicio
qtdNumeroPrimos = 0

while ((inicio <= numero) and (numero <= fim)):
    i = 1
    np = 0
    
    while (i <= numero):
        if (numero % i == 0):
            np += 1
        i += 1
      
    if (np == 2):
        print(numero)
        qtdNumeroPrimos += 1
        
    numero += 1

print('primos: '+str(qtdNumeroPrimos))
