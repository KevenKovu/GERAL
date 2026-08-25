preco_pao = float(input("Digite o preço do pão: "))

print("Tabela de preços")

for i in range(1, 51):
    preco_total = i * preco_pao
    print(f"{i} - R$ {preco_total:.2f}")