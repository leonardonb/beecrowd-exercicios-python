N = int(input())
mochila = []
for i in range(N):
    mochila.append(input())

mochila = set(mochila)
pokemon = 151 - len(mochila)
print(f"Falta(m) {pokemon} pomekon(s).")
