B = int(input())
T = int(input())

final_do_corte = (B+T) * 35
m = 11200-final_do_corte

if final_do_corte > m:
    print(1)
elif m > final_do_corte:
    print(2)
else:
    print(0)
