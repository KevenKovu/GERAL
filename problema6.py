n = int(input("Qual o número o termo?"))
ant1=0
ant2=0
for i in range(0 , n):
    if i == 0 :
        atual =1
        ant2 =atual
    elif i==1:
        atual=1
        ant1 = atual
    else:
        atual= ant1 + ant2
        ant1 = ant2
        ant2=atual
        
print(atual)
  