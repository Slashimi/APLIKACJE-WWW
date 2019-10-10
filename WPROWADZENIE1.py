

tekst = 'Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker'
imie = 'Filip'
nazwisko = 'Szarejko'
litera1 = imie[2]
litera2 = nazwisko[3]
print(tekst)
print('w tekscie jest %i liter %s oraz %i liter %s'% (tekst.count(litera1), litera1,tekst.count(litera2), litera2))
