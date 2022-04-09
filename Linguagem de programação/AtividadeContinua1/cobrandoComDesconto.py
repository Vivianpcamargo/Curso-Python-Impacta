preco = float(input())
qtd = int(input())

valor = preco * qtd
valorDesconto = valor * (0.1 + (qtd * 0.01))
valorFinal = valor - valorDesconto

print(f'{valor:.2f}')
print(f'{valorFinal:.2f}')
