'''
6. Citește de la tastatură:
- numele;
- prenumele.
Afișează: 'Numele complet are x caractere'.
'''
import string

# nume=input('Introduceti numele dumneavoastra:')
# prenume=input('Introduceti prenumele :')
# print(f'Numele dumneavoastra este{nume} {prenume} ')
# print( f'Numele dumneavoatra este {nume} {prenume} si are {len(nume + prenume)} caractere')
#
'''
Citește de la tastatură:
- lungimea;
- lățimea.
Afișează: 'Aria dreptunghiului este x'.

'''
# lungimea = int(input('Introduceti lungimea triunghiului: '))
# latimea = int(input('Introduceti latimea triunghiului: '))
# Inaltimea = float(input('Introduceti inaltimea triunghiului:'))
# Aria = (lungimea+latimea)/Inaltimea
# print(f'Aria triunghiului este: {Aria}') FUNTCTIONAL

#INTRODUCEREA DE LA TASTATURA A DATELOR

# lungimea= float(input('Introduceti lungimea dreptunghiului: '))
# latimea = float(input('Introduceti latimea dreptunghiului '))
# aria= lungimea * latimea
# print(f'Aria dreptunghiului este {aria}')
#FUNCTIONAL

'''
8. Având stringul: 'Coral is either the stupidest animal or the smartest rock':
- afișează de câte ori apare cuvântul 'the';
'''
string_prop= 'Coral is either the stupidest animal or the smartest rock'
print(string_prop.count('the'))
'''
Același string.
● Folosiți un assert ca să verificați dacă acest string conține doar numere.

'''
propx = 'Coral is either the stupidest animal or the smartest rock'
assert propx.isdigit()is True,'Propozitia nu contine numere'
