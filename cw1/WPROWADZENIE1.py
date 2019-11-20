#CWICZENIE_1

tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'

#CWICZENIE_2

imie = 'Filip'
nazwisko = 'Szarejko'
litera1 = imie[2]
litera2 = nazwisko[3]

print('w tekscie jest %i liter %s oraz %i liter %s'% (tekst.count(litera1), litera1,tekst.count(litera2), litera2))

#CWICZENIE_3

a = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce a iaculis lacus, et scelerisque erat."
b = a.replace("Lorem", "lacina1").replace("ipsum", "lacina2")
print(b)
a2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit.".upper()
print(a2)
a3 = "LOREM!".lower()
print(a3)
a4 = "LOrem1"
a4 = list(a4)[2:-2]
print("".join(a4))
a5 = "Lorem ipsum dolor sit amet, consectetur adipiscing eliT."
print(a5[0], a5[-1])

#CWICZENIE_4

zmienna_typu_string="elit"
print(dir(zmienna_typu_string))
help(zmienna_typu_string.casefold)

#CWICZENIE_5

print(imie[::-1]);
print(nazwisko[::-1]);

#CWICZENIE_6

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
nowaLista = [];
nowaLista = lista[5:10];
del lista[5:10];
print(lista);
print(nowaLista);

#CWICZENIE_7

kolejnaLista1 = lista + nowaLista;
kolejnaLista1.insert(0, 0);
kolejnaLista2 = kolejnaLista1.copy();
kolejnaLista2.sort();
kolejnaLista2.reverse();
print(kolejnaLista1);
print(kolejnaLista2);

#CWICZENIE_8

student1=(123123, 'Dawidewicz')
student2=(696969, 'Bodziech')
student3=(696420, 'Żużlini')
student4=(654321, 'Artom')
student5=(183057, 'Nowak')

lista=[student1,student2,student3,student4,student5]
print(lista)
#CWICZENIE_9

studnet6 = dict(wiek=19,
                email='aaaaa@bbb.pl',
                adres='Olsztyn'
                )
studnet6 = dict(wiek=22,
                email='hwdp@jp100.pl',
                adres='Gietrzwałd'
                )

#CWICZENIE_10

powtorzenia = ["123456789", "826492873", "123456789", "819302719", "123456789"]
powtorzenia = set(powtorzenia)
print(powtorzenia)

#CWICZENIE_11

for i in range(11):
    print(i)

#CWICZENIE_12

for i in range(20, 105, 5).__reversed__():
    print(i)

#CWICZENIE_13

ostatnie = [{"adin": 1, "dwa": "totaksamo"}, {"tri": 3, "niemam": 12123310}, {"cyrylicy": 6, 6: "naklawie"}]
string = ""
for x in ostatnie:
    for y in x.keys():
        string += str(x[y]) + " "
print(string)

