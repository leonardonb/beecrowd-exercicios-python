def codigo(x):
    if x in 'GQaku': 
        return 0
    if x in 'ISblv': 
        return 1
    if x in 'EOYcmw': 
        return 2
    if x in 'FPZdnx': 
        return 3
    if x in 'JTeoy': 
        return 4
    if x in 'DNXfpz': 
        return 5
    if x in 'AKUgq': 
        return 6
    if x in 'CMWhr': 
        return 7
    if x in 'BLVis': 
        return 8
    if x in 'HRjt': 
        return 9

N = int(input())

for i in range(N):
    senha = str(input()).replace(' ', '')
    cripto = ''
    for j in senha:
        cripto += str(codigo(j))
        
    print(cripto[:12])
