def escrever():



    pass
with open("votos.txt","r") as arquivo:
    v= arquivo.readlines()
    vlista= [0,0,0,0,0,0]
    for i in range(0,len(v)):
        try:
            a= v[i]
            v[i]=a.replace("\n","")
        except:
            print("erro")
        r = int(v[i])
        for j in range(0,5):
            if r == int(j+1):
                vlista[j]=vlista[j] + 1
        if r > 5 or r< 1 :
            vlista[5]=int(vlista[5]) +1
    mv=0
    Mv=0
    print(vlista)
    print(Mv,mv)

