con= int(input("Quantos alunos?"))
lista=[None]*con
with open("texto.txt","w") as arquivo:

    for i in range(0,con):
        lista[i]= f"\n{input('Escreva a matricula, apenas um sobrenome e o ano de nascimento do aluno. Dando um espaço entre os dados. :) ')}"
        arquivo.write(lista[i])
    for j in lista: 
        print(j)
