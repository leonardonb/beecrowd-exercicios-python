C = int(input())
escolha_vitoriosa = {"pedra": ["tesoura", "lagarto"], "papel": ["pedra", "spock"], "tesoura": ["papel", "lagarto"], "lagarto": ["papel", "spock"], 
                     "spock": ["pedra", "tesoura"]}

for x in range(C):
    rajesh, sheldon = input().split()

    if(rajesh == sheldon):
        print("empate")
    elif(sheldon in escolha_vitoriosa[rajesh]):
        print("rajesh")
    else:
        print("sheldon")
