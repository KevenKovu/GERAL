with open("classe.txt", "r") as arquivo:
    classe = arquivo.readlines()
    for i in range(0,len(classe)):
        separar= classe[i].split(" ")
        classe[i] = separar
        try:
            a= classe[i][1]
            classe[i][1]=a.replace("\n","")
        except:
            print("erro")   
with open("notas.txt", "r") as arquivo:
    notas = arquivo.readlines()
    for j in range(0,len(notas)):
        separa= notas[j].split(" ")
        notas[j] = separa
        try:
            b= notas[j][4]
            notas[j][4]=b.replace("\n","")
        except:
            print("erro")   
r="s"
while r=="s":
    n=str(input("Qual o nome ou numero a pesquisar?"))
    for y in range(0,len(classe)):
        if classe[y][1]==n:
            l= classe[y][0]
        elif  classe[y][0]==n:
            l =classe[y][0]
    for x in range(0,len(notas)):
        if notas[x][0]==l:
            print(notas[x])
    r=str(input("Deseja continuar essa pesquisa?"))
listaluno=[None]*10
for p in range(0,10):
    listaluno[p]=input(str("insira um nome: "))
linhafim=int(classe[-1][0])
for e in range(0,10):
    classe+=[[linhafim + e ,listaluno[e]]]
    notas+= [[linhafim +e ,str(input(f"Quais são as notas do aluno {listaluno[e]}?")),str(input()),str(input()),str(input())]]
with open("classe.txt", "a") as arquivoc:
    with open("notas.txt", "a") as arquivon:
        for r in range(0,10):
            q=linhafim+int(r)
            arquivoc.write(f"\n{classe[q][0]} {classe[q][1]}")
            arquivon.write(f"\n{notas[q][0]} {notas[q][1]} {notas[q][2]} {notas[q][3]} {notas[q][4]}")
