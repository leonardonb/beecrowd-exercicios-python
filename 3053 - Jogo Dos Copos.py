def movimento(pos_atual, jogada):

    if (jogada == 1):
        v1, v2 = "A", "B"
    elif (jogada == 2):
        v1, v2 = "B", "C"
    elif (jogada == 3):
        v1, v2 = "A", "C"

    if pos_atual == v1:
        return v2
    elif pos_atual ==v2:
        return v1
    else:
        return pos_atual
    
N = int(input())
pos_atual = input()

for m in range(N):

    jogada = int(input())
    pos_atual = movimento (pos_atual, jogada)

print (pos_atual)
