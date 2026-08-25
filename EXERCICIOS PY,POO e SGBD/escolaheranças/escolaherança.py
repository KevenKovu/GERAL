class Turma:
    def __init__(self,cod,cur,ano)-> None:
        self.codigo = cod
        self.curso = cur
        self.ano = ano
        self.listaAlunos = []



    def listaNotas(self,nota) -> list:
        pass

    
    def addAluno(self,alu) -> None:
        self.listaAlunos += [alu]

class Aluno:
    def __init__(self,r,n,d):
        self.RA = r
        self.nome = n
        self.nasc = d

