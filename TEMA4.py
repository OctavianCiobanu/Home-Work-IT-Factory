'''
1.Având lista:
mașini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun',
'Fiat', 'Trabant', 'Opel']
Folosește un for că să iterezi prin toată lista și să afișezi;
● ‘Mașina mea preferată este x’.
● Fă același lucru cu un for each.
● Fă același lucru cu un while.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
''' FOR EACH'''
# for masina in masini:
#     print(f'Masina mea preferata este {masina}')
'''FOR'''
# for i in range(len(masini)):
#     print(f'Masina mea preferata este {masini[i]}')
'''WHILE'''
# j=0
# while j < len(masini):
#     j+=1
#     print(f'Masina mea preferata este {masini[j]}')
'''
2. Aceeași listă:
Folosește un for else
În for
- Modifică elementele din listă astfel încât să fie scrie cu majuscule,
exceptând primul și ultimul.
În else:
- Printează lista.
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# '''FOR'''
# for i in range(1,len(masini)-1):
#     masini[i] = masini[i].upper()
# else:
#     print(masini)

'''
3. Aceeași listă:
Vine un cumpărător care dorește să cumpere un Mercedes.
Itereaza prin ea prin modalitatea aleasă de tine.
Dacă mașina e mercedes:
Printează ‘am găsit mașina dorită de dvs’
Ieși din ciclu folosind un cuvânt cheie care face acest lucru
Altfel:
Printează ‘Am găsit mașina X. Mai căutam‘

'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun','Fiat', 'Trabant', 'Opel']
# for i in (masini):
#     if i == 'Mercedes':
#         print(f'Am gasit masina {i} dorita de dumneavoastra ')
#         break
#     else:
#        print(f'Am gasit masina {i} , mai cautam')

'''
4. Aceași listă;
Vine un cumpărător bogat dar indecis. Îi vom prezenta toate mașinile cu
excepția Trabant și Lăstun.
- Dacă mașina e Trabant sau Lăstun:
Folosește un cuvânt cheie care să dea skip la ce urmează (nu trebuie
else).
- Printează S-ar putea să vă placă mașina x.

'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lăstun', 'Fiat', 'Trabant', 'Opel']
# for masina in masini:
#     if masina == 'Trabant' or masina =='Lăstun':
#         continue
#     print(f'S-ar putea sa va placa masina :{masina}')

'''
5. Modernizează parcul de mașini:
● Crează o listă goală, masini_vechi.
● Itereaza prin mașini.
● Când găsesti Lăstun sau Trabant:
- Salvează aceste mașini în masini_vechi.
- Suprascrie-le cu ‘Tesla’ (în lista inițială de mașini).
'''
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
# for masini_vechi in masini:
#     if masini_vechi == 'Trabant' or masini_vechi == 'Lastun':
#             print(f'Masini vechi:{masini_vechi}')
''' Inlocuire elemente lista'''
# masini.remove('Lastun')
# masini.remove('Trabant')
# masini.insert(5,'Tesla')
# masini.insert(7, 'Tesla')
# print(f'Masini noi:{masini}')

'''
6. Având dict:
pret_masini = {
'Dacia': 6800,
'Lăstun': 500,
'Opel': 1100,
'Audi': 19000,
'BMW': 23000
}
Vine un client cu un buget de 15000 euro.
● Prezintă doar mașinile care se încadrează în acest buget.
● Itereaza prin dict.items() și accesează mașina și prețul.
● Printează Pentru un buget de sub 15000 euro puteți alege mașină
xLastun
● Iterează prin listă.
'''
# pret_masini = {
# 'Dacia': 6800,
# 'Lastun': 500,
# 'Opel': 1100,
# 'Audi': 19000,
# 'BMW': 23000}
# client={
# 'buget':15000}
# for i,j in pret_masini.items():
#     for a,b in client.items():
#         if j >=b:
#             print(f'{i}:{j}')
#         else:
#             print(f'Pentru un buget sub {b},avem disponibila masina {i}')

'''
7. Având liSTA
 numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
● Iterează prin ea.
● Afișează de câte ori apare 3 (nu ai voie să folosești count).
'''
#AFISEAZA DOAR 3
# numere = [5, 7, 3, 9, 3, 3, 1, 0, -4,3]
# duplicate=[]
# for i in numere:
#     if i not in duplicate:
#         duplicate.append(i)
#     else:
#         print(i)
#         break
#         print(len(duplicate(i)))


'''
8. Aceeași listă:
● Iterează prin ea
● Calculează și afișează suma numerelor (nu ai voie să folosești sum).
'''
# numere=[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# total1=0
# for i in range(len(numere)):
'''ADUNARE LISTA'''
#         total1=total1+numere[i]
# print(total1)

'''
9. Aceeași listă:
● Iterează prin ea.
● Afișază cel mai mare număr (nu ai voie să folosești max).
'''
# numere=[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# maxx=0
# for i in range(len(numere)): # 5       #7   --> 3
#         if maxx < i:          # 0<5 A  #  5 <7 F -->7<3 F
#                 maxx=i        # maxx=5 --> maxx=7 --> maxx=7
# print(maxx)

'''
10. Aceeași listă:
● Iterează prin ea.
● Dacă numărul e pozitiv, înlocuieste-l cu valoarea lui negativă.
'''
# numere=[5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
# neg=0
# for i in numere:
#     if neg < i :   #0 --> -5
#         neg= i - (i*2) # -5 --> -3
#         print(neg)

'''
1.
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
Itereaza prin listă alte_numere
Populează corect celelalte liste
Afișeaza cele 4 liste la final

'''
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []
for i in range(len(alte_numere)):
    if i % 2 == 0: