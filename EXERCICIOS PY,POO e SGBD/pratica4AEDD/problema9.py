somp = 0
somi = 0

while True:
    num = int(input("Digite um número: "))
    if num < 0:
        break
    if num % 2 == 0:
        somp += num
    else:
        somi += num

print("Soma dos números pares: ", somp)
print("Soma dos números ímpares: ", somi)
