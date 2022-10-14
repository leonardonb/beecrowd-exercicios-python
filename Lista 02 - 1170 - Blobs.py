N = int(input())

for x in range(N):
    C = float(input())
    i=0
    while (C>1):
        C/=2
        i+=1
    print(f"{i} dias")
