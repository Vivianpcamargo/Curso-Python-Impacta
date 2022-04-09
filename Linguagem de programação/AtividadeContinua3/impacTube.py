qntdCanais = int(input())

matrix = []
i = 0
j = 0
qntdInscritos = 1
monetizacao = 0
bonificacao = 0

while i < qntdCanais:
    inputUsuario = input().split(';')

    matrix.append(inputUsuario)

    i += 1
    
x = float(input())
y = float(input())

print('-----\nBÔNUS\n-----')

while j < qntdCanais:
    qntdInscritos = int(matrix[j][1]) // 1000
    monetizacao = float(matrix[j][2])

    if 'sim' == matrix[j][3]:
        milInscritos = qntdInscritos * x
    else:
        milInscritos = qntdInscritos * y

    if int(matrix[j][1]) >= 1000:
        bonificacao = monetizacao + milInscritos
    else:
        bonificacao = monetizacao

    print(matrix[j][0]+f': R$ {bonificacao:.2f}')

    j += 1