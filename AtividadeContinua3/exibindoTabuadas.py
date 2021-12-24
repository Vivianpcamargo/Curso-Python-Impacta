numero1 = int(input())
numero2 = int(input())
i = numero1

while i <= numero2:
    for x in range(11):
        if x != 0:
            resultado = i * x
            print(str(i)+' x '+str(x)+' = '+str(resultado))
    print('----------')
    i = i + 1

if numero1 > numero2:
    print('Nenhuma tabuada no intervalo!')