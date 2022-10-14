letra = input()
palavra = input().split()
soma_letra = 0.0
for x in palavra:
    if letra in x:
        soma_letra += 1

soma_letra /= len(palavra)/100

print('%.1f' % soma_letra)
