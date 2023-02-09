'''
 /*
        o variabila este o cutie de valori
        o variabila este o zona a memoriei in care tinem date
         */
'''
'''
2.Declară și initializează câte o variabilă din fiecare din următoarele tipuri de
variabilă :
- string
- int
- float
- bool
3. Utilizează funcția type pentru a verifica dacă au tipul de date așteptat
'''
numeTema='fds'
numar_tema=1
Numartema=3.4
Tema=True
print(type(numar_tema))
print(type(numeTema))
print(type(Tema))
print(type(Numartema))

'''
4. Rotunjește ‘float’-ul folosind funcția round() și salvează această modificare în
aceeași variabilă (suprascriere):
- Verifică tipul acesteia
'''
nr=4.33
print(f'Numarul float este {nr}')
nr=4.555
round(nr)
print(f'Numarul rotunjit este {round(nr)}')
print(type(nr))
'''
5.Folosește print() și printează în consola 4 propoziții folosind cele 4 variabile.
'''
banca='BRD'
bani_retrasi=300.5
bani_depusi=20
bani=False
print(f'Am mers la banca {banca} si am depus {bani_depusi} lei si am retras {bani_retrasi} lei insa am introdus pin-ul gresit si pe ecran mi-a aparut {bani} ')
