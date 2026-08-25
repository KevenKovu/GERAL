Algoritmo "maior3numeros"
//
//
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Keven Moreno Araújo
// Data atual  : 24/02/2022
Var
// Seção de Declarações das variáveis
   x, y, z: real

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc...
   escreva("Informe 3 numeros : ")
   leia(x,y,z)
   se(x>y)entao
               se(x>z)entao
                           escreva(x," é o maior.")
               senao
                    se(x=z)entao
                                escreva("Exitem números iguais.")
                    senao
                         escreva(z, " é o maior.")
                    fimse
               fimse
   senao
        se(x=y)entao
               escreva("Existem números iguais")
        senao
             se(y>z)entao
                    escreva(y, " é o maior.")
             senao
                  se(y=z)entao
                         escreva(z, " é o maior.")
                  fimse
             fimse
        fimse
   fimse
Fimalgoritmo