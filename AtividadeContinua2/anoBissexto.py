inicio = int(input())
fim = int(input())

ano = inicio
qtdBissexto = 0

while ((inicio <= ano) and (ano <= fim)):
	if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
		print(ano)
		qtdBissexto += 1
	ano += 1
print('bissextos: '+str(qtdBissexto))
