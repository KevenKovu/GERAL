class Caixa:
    def __init__(self, numero, setinha):
        self.numero = numero
        self.setinha = setinha


inicio = Caixa(1, None)
final = inicio
for numero in range(2, 5):
    final.setinha = Caixa(numero, None)
    final = final.setinha
inicio.setinha=inicio.setinha.setinha