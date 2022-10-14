for n in range(int(input())):
    
    entrada=input()
    i=0
    
    if len(entrada)==5:
        print("3")
    else:
        if entrada[0]=='o':
            i+=1
        if entrada[1]=='n':
            i+=1
        if entrada[2]=='e':
            i+=1

        if (i>=2):
            print("1")  
        else:
            print("2")
