C = int(input())

while(C > 0):
    C -= 1
    B, E = input().split()
    S = ""

    for x in range(int(B), int(E)+1):
       S += str(x)
    S += S[::-1]
    print(S)
