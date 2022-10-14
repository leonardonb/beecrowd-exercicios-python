alfab = 'abcdefghijklmnopqrstuvwxyz'
permut_inv = input()
frase = input()
for x in frase:
   print(alfab[permut_inv.find(x)], end="")
print ()
