# Programação Orientada a Objetos
# AC01 ADS-EaD - Números especiais
#
# Email Impacta: vivian.camargo@aluno.faculdadeimpacta.com.br

def eh_primo(n):
    contador = 0

    for i in range(1, n+1):
        if n % i == 0:
            contador += 1

    if contador == 2:
        return True
    else:
        return False


def lista_primos(n):
    lista = []

    for i in range(2, n):
        if eh_primo(i):
            lista.append(i)

    return lista


def conta_primos(s):
    tupla = {}

    for i in s:
        if eh_primo(i):
            if i in tupla:
                tupla[i] = tupla[i] + 1
            else:
                tupla[i] = 1

    return tupla


def eh_armstrong(n):
    soma = 0
    qntd = len(str(n))

    aux = n
    while aux > 0:
        digit = aux % 10
        soma += digit ** qntd
        aux //= 10

    if soma == n:
        return True
    else:
        return False


def eh_quase_armstrong(n):
    soma = 0
    qntd = len(str(n))

    aux = n
    while aux > 0:
        digit = aux % 10
        soma += digit ** qntd
        aux //= 10

    if soma - 1 == n or soma + 1 == n:
        return True
    else:
        return False


def lista_armstrong(n):
    lista = []

    for i in range(n):
        if eh_armstrong(i):
            lista.append(i)

    return lista


def eh_perfeito(n):
    contador = 0

    for i in range(1, n):
        if n % i == 0:
            contador += i

    if contador == n:
        return True
    else:
        return False


def lista_perfeitos(n):
    lista = []

    for i in range(1, n):
        if eh_perfeito(i):
            lista.append(i)

    return lista
