entradaX = input()
entradaY = input()

blocoX = []
blocoY = []

blocoX.extend(entradaX)
blocoY.extend(entradaY)

if (blocoX[0] != blocoY[0] and blocoX[2] != blocoY[2] and blocoX[4] != blocoY[4] and blocoX[6] != blocoY[6] and blocoX[8] != blocoY[8]):
    print ("Y")
else:
    print ("N")
