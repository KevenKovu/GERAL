with open("q2entrevista.txt","r") as arquivo:
    lista=arquivo.readlines()

for i in range(0,len(lista)):
    separar=lista[i].split(",")
    lista[i]=separar
    try:
        a= lista[i][3]
        lista[i][3]=a.replace("\n","")
    except:
        print("erro")

contF=0
ZF=0
for j in range(0,len(lista)):
    if lista[j][0]=="F":
        contF+=1
        if lista[j][2]=="N":
            if lista[j][3] == "S":
                idade=int(lista[j][1])
                if idade>40:
                    ZF+=1
contM=0
ZM=0
for y in range(0,len(lista)):
    if lista[y][0]=="M":
        contM+=1
        if lista[y][2]=="S":
            idd=int(lista[y][1])
            if idd<40:
                ZM+=1
F= (contF/len(lista))*100
M=ZM/contM*100
VF=ZF/contF*100
print(F,M,VF)
with open("q2respostas.txt","a") as resparq:
    resparq.write(f"\n{F},{M},{VF}")