with open("text.txt" ,  "r") as arquivo:
    texto= arquivo.readlines()
    a=0
    b=""
    for i in range(0,len(texto)):
        texto[i]=texto[i].split(" ")
        if  float(texto[i][4]) > a:
            a = float(texto[i][4])
            b=texto[i]
    for r in b:
        print(f"{r} " ,end="")
    