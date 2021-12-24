unidade = float(input())
valorVC = 0
valorReais = 0

while (unidade != -1.0):
    valorVC = valorVC + unidade
    valorReais = valorReais + (unidade * 2.5)

    unidade = float(input())

print(f'VC$ {valorVC:.2f}')
print(F'R$ {valorReais:.2f}')