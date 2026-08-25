from modulo1 import replace
list = ["G", "T", "A", "C"]

flag = 1
while flag != 0:
    DNA = input("Digite o DNA: ")
    DNA = DNA.upper()
    for i in DNA:
        if i == "G" or i == "T" or i == "A" or i =="C":
            flag = 0
        else:
            flag = 1
            print("Código inválido")
            break
                
print(replace(DNA))