import os

def menu():
    global resp
    resp = int(input("\nEscolha uma das opções de operações a seguir:\n\n1- Soma\n2- Subtração\n3- Multiplicação\n4- Divisão\n5- Sair do programa\n\nQual opção você deseja? "))
    os.system("cls")

def soma(x, y):
    os.system("cls")
    return print(x+y)
def subtracao(x, y):
    os.system("cls")
    return print(x-y)
def multiplicacao(x, y):
    os.system("cls")
    return print(x*y)
def divisao(x, y):
    os.system("cls")
    return print(x/y)


x = int(input("Digite um inteiro: "))
y = int(input("Digite outro inteiro: "))
os.system("cls")

while True:
    menu()
    if resp == 1:
        soma(x, y)
    elif resp == 2:
        subtracao(x, y)
    elif resp == 3:
        multiplicacao(x, y)
    elif resp == 4:
        divisao(x, y)
    else:
        break