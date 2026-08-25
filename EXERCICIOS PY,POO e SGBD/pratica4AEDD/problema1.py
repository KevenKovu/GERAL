def pupulacao(nhA, txA, nhB, txB):
    txA=txA /100
    txB=txB /100
    i=0
    while nhA <nhB: 
        nhA = nhA *txA
        nhB = nhB *txB
        i+=1
    return i
a =float(input())
b =float(input())
c =float(input())
d =float(input())
print(pupulacao(a,b,c,d))
