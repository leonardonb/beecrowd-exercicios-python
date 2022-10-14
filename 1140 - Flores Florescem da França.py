while True:
    entrada=input().split()
    
    if len(entrada)==1 and len(entrada[0])==1 and entrada[0]=='*':
        break
    
    tamanho=len(entrada)
    frase=[]
    for i in range(tamanho):frase.append(entrada[i][0].upper())
    tamanho=len(frase)
    
    if (frase.count(frase[0])==tamanho):
        print("Y") 
    else:
        print("N")
