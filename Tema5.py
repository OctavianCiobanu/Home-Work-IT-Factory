'''
1.Funcție care să calculeze și să returneze suma a două numere
'''
# def suma(a,b):
#     s=a + b
#     print(f'Suma este: {s}')
# suma(3,5)
'''2'''
#def suma (a,b):
#     s= a + b
#     # a=int(input('Introduceti primul numar:'))
#     # b=int(input('Introduceti al doilea numar:'))
#     print (f'Suma dintr {a} si {b} este : {s}')
# a=int(input('Introduceti primul numar:'))
# b=int(input('Introduceti al doilea numar:'))
# suma(a,b)

'''
2. Funcție care sa returneze TRUE dacă un număr este par, FALSE pt impar
'''
# def par_impar(numar):
#     if numar >= 0:
#         print(f'Numarul {numar} este par')
#     else:
#         print(f'Numarul {numar} este impar.')
# num=int(input('Introduceti un numar:'))
# print(par_impar())
'''3. Funcție care returnează numărul total de caractere din numele tău complet.
(nume, prenume, nume_mijlociu)
'''
# def nr_nume(nume,prenume,nume_mijlociu):
#     suma_tot = len(nume)+len(prenume)+len(nume_mijlociu)
#     print(f'Numarul de caractele al numelui dumneavoastra este : {suma_tot}')
# nume= input('Introduceti numele dumneavoastra:')
# prenume= input('Introduceti prenumele:')
# nume_mijlociu= input('Introduceti numele mijlociu:')
# nr_nume(nume,prenume,nume_mijlociu)

''' 4. Funcție care returnează aria dreptunghiului '''
''' Mod 1'''
# def aria_triunghi():
#     a=L*l
#     print(f'Aria triunghiului este:{a}')
# l=int(input('Introduceti lungimea dreptunghiului:'))
# L=int(input('Introduceti latimea dreptunghiului: '))
# aria_triunghi()
'''mod 2'''
# def aria_dreptunghi(l,L):
#     a=l*L
#     print(f'Aria dreptunghiului este: {a}')
# aria_dreptunghi(2,5)

'''5. Funcție care returnează aria cercului'''
# def aria_cerc():
#     A=3.14 * R
#     print(f'Aria cercului este:{A}')
# R=float(input('Introduceti raza cercului:'))
# aria_cerc()
'''6. Funcție care returnează True dacă un caracter x se găsește într-un string dat
și Talse dacă nu găsește.'''
# def gasire_caracter():
#     nume=input('Introduceti un nume:')
#     a=input('Introduceti un caracter:')
#     if a in nume:
#         return True
#     else:
#         return False
# d=gasire_caracter()
# if d:
#     print(f'Caracterul este in cuvantul introdus')
# else:
#     print(f'Caracterul nu este in cuvant')

'''
7. Funcție fără return, primește un string și printează pe ecran:
● Nr de caractere lower case este x
● Nr de caractere upper case exte y
'''
# def string():
#     nume=str(input('Introduceti un string:'))
#     lower=0
#     upper=0
#     for i in nume:
#         if i.isupper():
#             upper +=1
#         elif i.islower():
#             lower +=1
#     print(f'Nr de caractere upper este : {upper}')
#     print(f'Nr de caractere lower este: {lower}')
#
# string()

'''
8. Funcție care primește o LISTA de numere și returnează o LISTA doar cu
numerele pozitive
'''
'''1'''
# def Lista(l1):
#     for i in l1:
#         if i >= 0:
#             print(i)
#     return l1
# Lista([2,8,9,-2,4,-5,-3,1,7,-6,-3])
'''2'''
#     l1=[3,5,-2,0,-1,-7,4,1,9,34,-7]
#     for i in l1:    #3
#         if i >= 0:               # 3> 0
#             print(i)          # 3
#
# Lista()

'''9. Funcție care nu returneaza nimic. Primește două numere și PRINTEAZA
● Primul număr x este mai mare decat al doilea nr y
● Al doilea nr y este mai mare decat primul nr x
● Numerele sunt egale '''

# def nr():
#     a=int(input())
#     b=int(input())
#     if a > b:
#         print(f'Nr {a} mai mare decat {b}')
#     elif b > a:
#         print(f'Nr {b} este mai mare decat {a}')
#     else:
#         print(f'Numerele  sunt egale.')
# nr()
# nr()

'''Funcție care primește un număr și un set de numere.
● Printeaza ‘am adaugat numărul nou în set’ + returnează True
● Printeaza ‘nu am adaugat numărul în set. Acesta există deja’ +
returnează False
'''
# def nr_set(a,s1):
#         if a  not in s1:
#             print(f'Am adaugat noul nr in set')
#             return True
#         elif a in s1:
#             print(f'Nu am adaugat noul nr in set. Acesta exista deja')
#             return False
# nr_set(4,{3,5,7,3,4,1,3})

'''HARD'''
'''1. Funcție care primește o lună din an și returnează câte zile are acea luna'''
def luna_an(luni):