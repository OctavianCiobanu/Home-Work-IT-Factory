'''
1.Clasa Cerc
Atribute: raza, culoare
Constructor pentru ambele atribute
Metode:
● descrie_cerc() - va PRINTA culoarea și raza
● aria() - va RETURNA aria
● diametru()
● circumferinta()
'''

#
# class Cerc:
# #CONSTRUCTOR
#     def __init__(self,raza,culoare):
#         self.raza = raza
#         self.culor=culoare
# #METODE
#     def descrie_cerc(self):
#         print(f'Cercul are raza {self.raza} si culoarea {self.culor}')
#     def getfieds(self):
#         print(self.descrie_cerc())
#         print(self.aria())
#         print(self.diametru())
#         print(self.circumferinta())
#     def aria(self):
#         return 3.14 * self.raza ** 2
#     def diametru(self):
#           return 2 * self.raza
#     def circumferinta(self):
#         return self.raza * 3.14 * 2
#
#
# cerc= Cerc(2,'rosu')
# print(f'Cercul are aria : {cerc.aria()}')
# print(f'Cercul are diametru: {cerc.diametru()}')
# print(f'Cercul are circumferinta: {cerc.circumferinta()}')
# cerc.getfieds()

'''
2. Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pentru toate atributele
Metode:
● descrie()
● aria()
● perimetrul()
● schimbă_culoarea(noua_culoare) - această metodă nu returneaza nimic.
Ea va lua ca și parametru o nouă culoare și va suprascrie atributul
self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei
descrie().
'''

# class Dreptunghi :
#     #ATRIBUTE
#     lungime= None
#     latime= None
#     culoare=None
#     #CONTRUCTOR
#     def __init__(self,lungime,latime,culoare1):
#         self.lungime=lungime
#         self.latime=latime
#         self.culoare=culoare1
#     #METODE
#     def descrie(self):
#         print(f'Latime:{self.latime}')
#         print(f'Lungime:{self.lungime}')
#         print(f'Culoare:{self.culoare}')
#     def arie(self):
#         return self.latime *self.lungime
#     def perimetru(self):
#         return  2 * self.lungime + 2 * self.latime
#     def schimba_culoare(self,noua_culoare):
#          self.culoare = noua_culoare
#
# drept = Dreptunghi(3,5,'bej')
# drept.descrie()
# print(f'Aria:{drept.arie()}')
# print(f'Perimetru:{drept.perimetru()}')
# drept.schimba_culoare('verde')
# drept.descrie()

'''
3. Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
● descrie()
● nume_complet()
● salariu_lunar()
● salariu_anual()
● marire_salariu(procent)
'''
# class Angajat:
#     #ATRIBUTE
#     nume=None
#     prenume=None
#     salariu=None
#     #Contructor
#     def __init__(self,name,first_name,salary):
#         self.nume = name
#         self.prenume = first_name
#         self.salariu = salary
#     #METODE
#     def descriere(self):
#         print(f'Nume:{self.nume}')
#         print(f'Prenume:{self.prenume}')
#         print(f'Salariu:{self.salariu}')
#     def nume_complet(self):
#         return self.nume +' '+ self.prenume
#     def salariu_lunar(self):
#         return self.salariu
#     def salariu_anual(self):
#         return self.salariu *12
#     def marire_salariu(self,procent):
#         return self.salariu_lunar() * (1 + procent/100)
# angajat= Angajat('Marius','Ciobanu',1500)
# angajat.descriere()
# print(angajat.nume_complet())
# print(angajat.salariu_lunar())
# print(angajat.salariu_anual())
# print(angajat.marire_salariu(10))

'''
4.Clasa Cont
Atribute: iban, titular_cont, sold
Constructor pentru toate atributele
Metode:
● afisare_sold() - Titularul x are în contul y suma de n lei
● debitare_cont(suma)
● creditare_cont(suma)
'''
# class Cont:
#     #ATRIBUTE
#     iban=None
#     titular_cont = None
#     sold= None
#     #CONTRUCTOR
#     def __init__(self,iban,titular,sold):
#         self.iban=iban
#         self.titular_cont=titular
#         self.sold=sold
#     def afisare_sold(self):
#         print(f'Titularul {self.titular_cont}  are în contul {self.iban} suma de {self.sold} lei)')
#     def debitare_cont(self,suma):
#         suma=self.sold - suma
#         return suma
#     def creditare_cont(self,suma):
#         return self.sold + suma
# cont1=Cont('RO0313456845400','Octavian Ciobanu',400)
# cont1.afisare_sold()
# print(f'Dupa debitare mai aveti in cont:{cont1.debitare_cont(300)} lei')
# print(f'Credit:{cont1.creditare_cont(3000)}')

'''
1. Clasa Factura
Atribute: seria (va fi constantă, nu trebuie constructor, toate facturile vor
avea aceeași serie), număr, nume_produs, cantitate, pret_buc
Constructor: toate atributele, fara serie
Metode:
● schimbă_cantitatea(cantitate)
● schimbă_prețul(pret)
● schimbă_nume_produs(nume)
● generează_factura() - va printa tabelar dacă reușiți
Factura seria x numar y
Data: generați automat data de azi
Produs | cantitate | preț bucată | Total
Telefon | 7 | 700 | 49000
'''
import datetime
curent_date_time = datetime.datetime.now().strftime("%d/%m/%Y")
class Factura:
    seria= 'ds358332'
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None
    def __init__(self,numar,nume_produs,cantitate,pret_buc):
        self.numar = numar
        self.nume_produs= nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc
    def schimba_cantiate(self,cantitate):
        cantitate= int(input('Introduceti cantitatea noua:'))
        return self.cantitate == cantitate
    def schimba_pretul(self,pret):
        pret= float(input('Introduceti noul pret:'))
        return self.pret_buc == pret
    def generare_factura(self,tabel):
       # curent_date_time=datetime.datetime.now().strftime("%d/%m/%Y")
        tabel =[ [ 'Factura' , self.seria , self.numar]
        [print(curent_date_time)]
        [self.nume_produs,'|',self.cantitate,'|',self.pret_buc,"Total"]
        ['Telefon | 7 | 700 | 49000']
        ]
