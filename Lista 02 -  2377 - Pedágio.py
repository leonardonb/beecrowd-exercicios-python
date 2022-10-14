L, D = map(int,input().split())

#L - Comprimento da estrada
#D - Distância entre pedágios

K, P = map(int,input().split())

#K - Custo por quilômetro percorrido
#P - Valor de cada pedágio

pedagios=int(L/D)

valor=(K*L)+(P*pedagios)

print(valor)
