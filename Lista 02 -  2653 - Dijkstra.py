joias = []

while True:
    try:
        joias.append(input())
        
    except EOFError:
        break
        
joias = set(joias)
print(len(joias))
