def rodaLista(input, lista):
    if len(input) > 1:
        for i in range(len(input)):
            if input[i] == 'encerrar' or input[i] == 'exibir' or input[i] == 'remover' or input[i] == 'adicionar':
                lista.append(input[i])
            else:
                lista.append(int(input[i]))
        return lista
    else: 
        return input

def exibir(carrinho, mensagem):
    carrinho.sort()

    if len(carrinho) > 0:
        mensagem.append(list(carrinho))

    return mensagem

def adicionar(index, carrinho):
    carrinho.append(index)
    carrinho.sort()

    return carrinho

def remover(index, carrinho, mensagem):
    contador = 0

    if index in carrinho:
        carrinho.remove(index)
        contador +=  1

    if contador == 0:
        mensagem.append('código '+str(index)+' não encontrado')

    return carrinho

carrinho = []
digitado = []
mensagem = []
lista = []

confereInput1 = input().split()
rodaLista(confereInput1, carrinho)

while digitado.count('encerrar') < 1:
    digitado.clear()

    confereInput2 = input().split()
    digitado = rodaLista(confereInput2, digitado)

    if 'exibir' in digitado[0]:
        mensagem = exibir(carrinho, mensagem)
    elif 'adicionar' in digitado[0]:
        carrinho = adicionar(int(digitado[1]), carrinho)
    elif 'remover' in digitado[0]:
        carrinho = remover(int(digitado[1]), carrinho, mensagem)

mensagem = exibir(carrinho, mensagem)

for x in range(len(mensagem)):
    if 'código' in mensagem[x]:
        print(mensagem[x])
    else:
        print(*mensagem[x])