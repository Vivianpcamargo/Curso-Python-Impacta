valorDivida = int(input())
valorMensal = int(input())

valorDepois = valorDivida
valorAntes = valorDepois
pagamento = 0

while (valorDepois != 0):
    pagamento += 1
    valorAntes = valorDepois
    
    if (valorAntes - valorMensal < 0):
    	valorDepois = valorDepois - valorAntes
    else:
     	valorDepois = valorAntes - valorMensal
    
    print('pagamento: '+str(pagamento))
    print('antes = '+str(valorAntes))
    print('depois = '+str(valorDepois))
    print('-----')