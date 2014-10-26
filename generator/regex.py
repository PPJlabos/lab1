
def novo_stanje(automat):
    automat.broj_stanja = automa.broj_stanja+1
    return automat.broj_stanja -1

def je_operator(izraz, i):
    br = 0
    while( i-1>0 && izraz[i-1] == )



# prebroji koliko ima \ u nizu prije znaka, ukoliko je broj paran (\\) onda je operator
# ukoliko je broj \ neparan (\) ona je znak, npr. \( -> je oznaka za zagradu dok je ( operator selekcije u izrazu ()
# \ se koristi kao escape oznaka, npr u C-u \\ -> znaci \, \n -> novi red \t -> tab \" navodnik unutar stringa print ("\"") -> "
def je_operator(izraz, i):
    br = 0
    while (i-1 >= 0 && izraz[i-1]=='\\') # broji escape oznake, ukoliko se pojavi nesto sto nije \ onda prekini provjeru
        br = br + 1
        i = i - 1       # gledamo unazad od znaka koji provjeravam
    return br&2 == 0    # ukoliko je broj znakova \ paran onda je znak operator, inace je znak





    # automat ce biti dict automat ime dicta ce biti genericko i vezano uz stanje -> dict(stanje lex analizatora, dict automata)
def pretvori(izraz, automat):
    izbori = []
    br_zagrada = 0; # pobroji kolicinu zagrada

    for i in range(len(izraz)):
        if izraz[i] == '(' && je_operator(izraz, i): # provjeri je li trenutni znak operator otvorena zagrada (
            br_zagrada++
        elif znak == ')' && je_operator(izraz, i):  # provjeri je li trenutni znak operator zatvorena zagrada )
            br_zagrada--
        elif br_zagrada == 0 && znak == '|' && je_operator(izraz, i):
            # TODO: Grupiraj lijevi negrupirani dio niza znakova izraza u niz izbor

    #TODO: ako je pronadjen barem jedan operator izbora
        # TODO: grupiraj preostali negrupirani dio niza znakova izraza u niz izbor

        lijevo_stanje = novo_stanje(automat)
        desno_stanje = novo_stanje(automat)
        if pronadjen_barem_jedan_operator:
            for element in izbori:
                _temp = pretvori(element ,automat)
                dodaj_e_prijelaz(automat, lijevo_stanje, _temp.lijevo_stanje)
                dodaj_e_prijelaz(automat, _temp.desno_stanje, desno_stanje)
        else:
            prefiksirano = False
            zadnje_stanje = lijevo_stanje
            for element in izbori:
                if prefiksirano:
                    #TODO: slucaj 1
                    prefiksirano = False
                    if element == 't':
                        prijelazn_znak = '\t' # oznaka za tabu u C-u
                    elif element == 'n':
                        prijelazn_znak = '\n'
                    elif element == '_':
                        prijelazn_znak = ' '
                    else:
                        prijelazn_znak = element

                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_e_prijelaz(automat, a, b, prijelazn_znak)

                else:
                    #TODO: slucaj 2
                    j = # TODO: pronadji odgovarajucu zatvorenu zagradu
                    _temp = pretvori( elementi , automat)
                    a = _temp.lijevo_stanje
                    b = _temp.desno_stanje
                    i = j

                if i+1 < izraz.length() && izraz[i+1] == '*':
                    x=a
                    y=b
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_e_prijelaz(automat, a, x)
                    dodaj_e_prijelaz(automat, y, b)
                    dodaj_e_prijelaz(automat, a, b)
                    dodaj_e_prijelaz(automat, y, x)
                    i++

                dodaj_e_prijelaz(automat, zadnje_stanje, a)
                zadnje_stanje = b
            dodaj_e_prijelaz(automat, zadnje_stanje, desno_stanje)
    return (lijevo_stanje, desno_stanje)
