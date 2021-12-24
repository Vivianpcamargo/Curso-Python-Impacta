numero = int(input())
alfabeto = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z')

for i in range(1, numero+1):
    for x in range (i):
        print(alfabeto[i-1], end='')
    print()