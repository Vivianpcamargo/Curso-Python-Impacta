# sobrecarga

def sobrecarga(nome, numero=None):
    print(nome)
    if numero:
        print(numero)


print('primeira execução')
sobrecarga('rafael')

print('\nsegunda execução')
sobrecarga('rafael', 10)
