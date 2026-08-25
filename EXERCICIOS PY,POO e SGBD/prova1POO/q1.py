from abc import ABC, abstractmethod

class PrismaRetoRegular:
    def __init__(self, figuraBase, figuraLateral):
        self.figuraBase = figuraBase
        self.figuraLateral = figuraLateral
    
    def calculaAreaSuperficie(self):
                areaBases = 2 * self.figuraBase.calculaArea()
                areaLateral = self.figuraBase.lado * self.figuraLateral.calculaArea()
                return areaBases + areaLateral
    def calculaVolume(self):
        	return self.figuraBase.calculaArea() * self.figuraLateral.altura
class FiguraRegular2D(ABC):
    def __init__(self, cor, lado):
            self.cor =cor
            self.lado = lado
    @abstractmethod
    def calculaArea(self):
            pass
            

class Lateral(FiguraRegular2D):
		def __init__(self, cor, lado, altura):
			super().__init__(cor, lado)
			self.altura = altura
			
		