'''
1. Explică cu cuvintele tale în cadrul unui comentariu cum funcționează un if
else.
if si else evalueaza conditii si bifurca codul in functie de rezultat
'''
'''
2. Verifică și afișează dacă x este număr natural sau nu.

'''
# numar=int(input('Introduceti un numar:'))
# if numar <0 :
#     print('Numarul nu este natural')
# else:
#     print('Numarul este natural')
'''
3. Verifică și afișează dacă x este număr pozitiv, negativ sau neutru.

'''
# x=int(input('Introduceti un numar: '))
# if x>0:
#     print('Numarul este pozitiv')
# elif x<0:
#     print('Numarul este negativ')
# elif x == 0:
#     print('Numarul este neutru')
# else:
#     print('Nu a-ti introdus niciun numar')
'''
4. Verifică și afișează dacă x este între -2 și 13
'''
# z=int(input('Introduceti un numar cuprins intre -2 si 13: '))
# if -2 <= z <=13:
#     print('Numarul introdus se afla intre -2 si 13')
# else:
#     print('Numarul introdus nu se afla intre -2 si 13')
'''
5. Verifică și afișează dacă diferența dintre x și y este mai mică de 5.
# '''
# nr1=int(input('Introduceti un numar x :'))
# nr2=int(input('Introduceti un numar y:'))
#
# if (nr1-nr2) < 5 :
#     print('Diferenta dintre x si y este mai mica decat 5')
# else:
#     print('Diferenta este mai mare decat 5')
'''
6. Verifică dacă x NU este între 5 și 27 - a se folosi ‘not’.
'''
# x=int(input('Introduceti un numar:'))
# if 5>x<27:
#     print("Numarul nu se afla intre 5 si 27")
# else:
#     print('Numarul se afla intre 5 si 27')
'''
x și y (int)
Verifică și afișează dacă sunt egale, dacă nu afișează care din ele este mai
mare.
# '''
# nr = int(input('Introduceti un numar:'))
# nr2= int(input('Introduceti al doilea numar:'))
# if nr == nr2:
#     print("Numerele sunt egale!")
# elif nr>nr2:
#     print(f'Numarul mai mare este {nr} ')
# elif nr<nr2:
#     print(f'Numarul mai mare este {nr2}')
# else:
#     print('Nu a-ti introdus o valoare corecta.')
'''

X, y, z - laturile unui triunghi.
Afișează dacă triunghiul este isoscel, echilateral sau oarecare.
'''
# l1=float(input('Introduceti latura 1 a triunghiului:'))
# l2 = float(input('Introduceti latura 2 a triunghiului:'))
# l3= float(input('Introduceti latura 3 a triunghiului:'))
# if l1 == l2 == l3:
#     print('Triunghiul este isoscel')
# elif l1 ==l2 or l2==l3 or l1==l3:
#     print('Triunghiul este echilateral')
# else:
#     print('Triunghiul este unul oarecare.')
'''
9. Citește o literă de la tastatură.
Verifică și afișează dacă este vocală sau nu
'''
# litera=input('Introduceti o litera')
# if litera == 'a' and 'e' and 'i' and 'o' and 'u':
#     print('Litera este o vocala')
# else:
#     print('Litera este o consoana')
'''
.Transformă și printează notele din sistem românesc în >
Peste 9 => A
Peste 8 => B
Peste 7 => C
Peste 6 => D
Peste 4 => E
4 sau sub => F

'''
# dex=float(input('Introduceti un numar de la tastatura: '))
# if 8<dex > 9:
#     print('A')
# elif dex >8:
#     print('B')
# elif dex > 7:
#     print('C')
# elif dex>6:
#     print ('D')
# elif dex> 5:
#     print('E')
# elif dex<4:
#     print ('F')
'''
1.Verifică dacă x are minim 4 cifre (x e int).
(ex: 7895 are 4 cifre, 10 nu are minim 4 cifre
'''
crt=int(input('Introduceti un numar de la tastatura:'))
if 4<cr <= crt:
    print(f'Numarul {crt} are minim 4 cifre:')
else:
    print(f'{crt} NU are 4 cifre')