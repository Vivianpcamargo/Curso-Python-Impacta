num = int(input())

numeros = {}
soma = 0
media = 0
i = 0

while num > 0:
    numeros[i] = num
    soma = soma + num
    i = i + 1
    num = int(input())

if i == 0:
    media = soma/1
else:
    media = soma/i

print(f'MEDIA: {media:.2f}')
        
for x in range(i):
    if numeros[x] < media:
        print(numeros[x])
