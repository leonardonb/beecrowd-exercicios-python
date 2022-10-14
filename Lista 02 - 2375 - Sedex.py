N = int(input())
altura, largura, profundidade = input().split()

if (N <= int(altura) and N <= int(largura) and N <= int(profundidade)):
    print('S')
else:
    print('N')
