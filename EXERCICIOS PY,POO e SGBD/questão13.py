# arquivo Geometria.py
class Ponto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __del__(self):
        print(f"lixo de memória: {self.x} {self.y}")

# arquivo Principal.py
#from Geometria import Ponto

def alteraDados(lista, obj):
    obj.x = 55
    obj = Ponto(3, 3)
    lista[0] = Ponto(6, 8)

obj1 = [None, None]
obj2 = Ponto(2, 4)
obj3 = Ponto(1, 2)
obj2 = obj3
obj3.x = 5
alteraDados(obj1, obj2)
print(f"x = {obj3.x} e y = {obj3.y}")
input("espera um pouco pra eu ver")