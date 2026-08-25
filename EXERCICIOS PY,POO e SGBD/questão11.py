class Aula:
    def __init__(self, data, hi, hf):
        self.data = data
        self.hi = hi
        self.hf = hf

class Professor:
    def __init__(self, nome, titulacao):
        self.nome = nome
        self.titulacao = titulacao

    def LancaNotas(self, RA:str):
        self.RA = RA
        pass