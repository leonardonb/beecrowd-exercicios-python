A,B,C,D = map(int,input().split())

if A < B + C and B < A + C and C < A + B:
    print('S')
elif A < B + D and B < A + D and D < A + B:
    print('S')
elif A < C + D and C < A + D and D < A + C:
    print('S')
elif B < C + D and C < B + D and D < B + C:
    print('S')
else:
    print('N')
