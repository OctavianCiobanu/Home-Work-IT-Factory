'''Clasa abstractă FormaGeometrica
Conține un field PI=3.14
Conține o metodă abstractă aria (opțional)
Conține o metodă a clasei descrie() - aceasta printează pe ecran ‘Cel mai
probabil am colturi’
'''
from abc import ABC , abstractmethod


class FormaGeometrica(ABC):
    PI= 3.14
    @abstractmethod
    def aria(self):
        raise NotImplementedError
    def descrie(self):
        print('Cel mai probabil am colturi')

'''2.Clasa Pătrat - moștenește FormaGeometrica
constructor pentru latură.'''

class Patrat(FormaGeometrica):
    def __init__(self,latura):
        self.latura = latura
#3.latura este proprietate privată.
#Implementează getter, setter, deleter pentru latură
#Implementează metoda cerută de interfață (opțional, doar dacă ai ales să
#implementezi metoda abstractă aria)
    __latura=3
    def get_latura(self):
        return self.__latura
    def set_latura(self,latura_noua):
        self.__latura = latura_noua
        print(f'Noua latura este {latura_noua}')
    def deleter_latura(self):
        print(f'Am stres latura')
        self.__latura= None
    def aria(self):
        return self.latura ** 2
    def descrie(self):
        print("Sunt un patrat")
'''Clasa Cerc - moștenește FormaGeometrica
constructor pentru rază
raza este proprietate privată
Implementează getter, setter, deleter pentru rază
Implementează metoda cerută de interfață - în calcul folosește field PI
mostenit din clasa părinte (opțional, doar dacă ai ales să implementezi metoda
abstractă aria'''
class Cerc(FormaGeometrica):
    def __init__(self,raza):
        self.__raza= raza

    def get_raza(self):
        return self.__raza
    def setter_raza(self,raza_noua):
        self.__raza = raza_noua
        print(f'Raza a fost schimbata in {raza_noua}')
    def deleter_raza(self):
        self.__raza= None
        print('Am sters raza')
    def aria(self):
       return FormaGeometrica.PI * (self.__raza **2)
#Definește o nouă metodă descrie - printează ‘Eu nu am colturi’
#Creează un obiect de tip Patrat și joacă-te cu metodele lui
#Creează un obiect de tip Cerc și joacă-te cu metodele lui
    def descrie(self):
        print('Eu nu am colturi')
patrat = Patrat(2)
patrat.descrie()
print(f'Aria patratului este: {patrat.aria()}')
patrat.set_latura(6)
cerc = Cerc(4)
cerc.descrie()
print(f'Aria cercului este: {cerc.aria()}')