notaTrabalho = float(input())
notaProva = float(input())

nota = (notaTrabalho + notaProva) / 2

if nota >= 6:
    print('aprovado')
else:
    podeTentar = 0

    for notaSubstitutiva in range(10):
        if ((notaTrabalho + notaSubstitutiva) / 2) >= 6:
            podeTentar += 1

    if podeTentar > 0:
        print('talvez com a sub')
    else:
        print('reprovado')
