with open("q3entrevista.txt","r") as arquivo:
    lista=arquivo.readlines()

for i in range(0,len(lista)):
    separar=lista[i].split(",")
    lista[i]=separar
    try:
        a= lista[i][5]
        lista[i][5]=a.replace("\n","")
    except:
        print("erro")

contF=0
ZF=0
gostadejilo=0
for j in range(0,len(lista)):
    if lista[j][0]=="F":
        contF+=1
        if lista[j][2]=="N":
            if lista[j][3] == "S":
                idade=int(lista[j][1])
                if idade>40:
                    ZF+=1
                    if  lista[j][4]=="S":
                        gostadejilo+=1 #chata

contM=0
ZM=0
assassino=0
for y in range(0,len(lista)):
    if lista[y][0]=="M":
        contM+=1
        if lista[y][2]=="S":
            idd=int(lista[y][1])
            if idd<40:
                ZM+=1
                if lista[y][5]=="S":
                    assassino+=1 #se é assassino
for m in range(0,len(lista)):
    if lista[y][5]=="S":
            assassino+=1 #se é assassino
    if  lista[j][4]=="S":
                        gostadejilo+=1 #chata

F= (contF/len(lista))*100
M=ZM/contM*100
VF=ZF/contF*100
Fchata=gostadejilo/len(lista)*100
Mssino=assassino/len(lista)*100
print(F,M,VF)
with open("q3respostas.txt","a") as resparq:
    resparq.write(f"\n{F},{M},{VF},{Fchata},")