N = int(input())

for i in range(N):
    texto = input()
    entradas = texto.split(' ')
    decodificado = ""

    index = 0

    while index <= len(entradas[0]) - 1 or index <= len(entradas[1]) - 1:
        if index <= len(entradas[0]) - 1:
          decodificado += entradas[0][index]
        if index <= len(entradas[1]) - 1:
            decodificado += entradas[1][index]
        
        index += 1
    
    print (decodificado)
