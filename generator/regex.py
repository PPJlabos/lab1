# kao neki brojac stanja u automatu
def novo_stanje(automat):
    automat[len(automat)+1] = ""
    return len(automat)



# prebroji koliko ima \ u nizu prije znaka, ukoliko je broj paran (\\) onda je operator
# ukoliko je broj \ neparan (\) ona je znak, npr. \( -> je oznaka za zagradu dok je ( operator selekcije u izrazu ()
# \ se koristi kao escape oznaka, npr u C-u \\ -> znaci \, \n -> novi red \t -> tab \" navodnik unutar stringa print ("\"") -> "
def je_operator(izraz, i):
    br = 0
    while i-1 >= 0 and izraz[i-1]=='\\': # broji escape oznake, ukoliko se pojavi nesto sto nije \ onda prekini provjeru
        br = br + 1
        i = i - 1       # gledamo unazad od znaka koji provjeravam
    return br&2 == 0    # ukoliko je broj znakova \ paran onda je znak operator, inace je znak



def dodaj_prijelaz(automat ,stanje1, stanje2, znak):
    automat[str(stanje1)+znak] = stanje2

def nadi_iducu_zagradu(izraz, i):
    br_zagrada = 1
    for izraz[j] in range( len (izraz[i+1:])):
        if izraz[j] == ")" and je_operator (izraz, j):
            br_zagrada -= 1
            if br_zagrada == 0:
                return j
        elif izraz[j] == "(" and je_operator(izraz, j):
            br_zagrada += 1

    return i





    # automat ce biti dict automat, ime dicta ce biti genericko i vezano uz stanje -> dict(stanje lex analizatora, dict automata)
def pretvori(izraz, automat):
    e = "$"
    izbori = []
    elementi = []
    br_zagrada = 0 # pobroji kolicinu zagrada zasto se broje zagrade i kako se pretvaraju
    _a = 0
    pronadjen_barem_jedan_operator = False
    for i in range(len(izraz)):
        if izraz[i] == '(' and je_operator(izraz, i): # provjeri je li trenutni znak operator otvorena zagrada (
            br_zagrada += 1

        elif izraz[i] == ')' and je_operator(izraz, i):  # provjeri je li trenutni znak operator zatvorena zagrada )
            br_zagrada -= 1
            # ako naidjes na izraz oblika (ab)|c razdvoji izraz na ['(ab)', 'c']
        elif br_zagrada == 0 and izraz[i] == '|' and je_operator(izraz, i):
            izbori.extend(izraz[_a:i])
            print izbori.extend(izraz[_a:i])
            pronadjen_barem_jedan_operator = True
            _a=i

    lijevo_stanje = novo_stanje(automat)
    desno_stanje = novo_stanje(automat)

    if pronadjen_barem_jedan_operator:
        for element in izbori:
            _temp = pretvori(element ,automat)
            dodaj_prijelaz(automat, lijevo_stanje, _temp[0], e)
            dodaj_prijelaz(automat, _temp[1], desno_stanje, e)
    else:
        prefiksirano = False
        zadnje_stanje = lijevo_stanje
        for element in izraz:
            if prefiksirano:
                # slucaj 1
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
                dodaj_prijelaz(automat, a, b, e)#, prijelazn_znak)
            else:
                # slucaj 2
                # TODO: pronadji odgovarajucu zatvorenu zagradu
                j = nadi_iducu_zagradu(izraz, i)
                _temp = pretvori( elementi , automat)
                a = _temp[0]
                b = _temp[1]
                i = j
            if i+1 < len(izraz) and izraz[i+1] == '*':
                y=b
                a = novo_stanje(automat)
                b = novo_stanje(automat)
                dodaj_prijelaz(automat, a, x, e)
                dodaj_prijelaz(automat, y, b, e)
                dodaj_prijelaz(automat, a, b, e)
                dodaj_prijelaz(automat, y, x, e)
                i += 1
            dodaj_prijelaz(automat, zadnje_stanje, a, e)
            zadnje_stanje = b
    return (lijevo_stanje, desno_stanje)

automat = {}
print pretvori("a|b|(acs|S)|\\t|w*", automat)
for key in automat.keys():
    print str(key) + ":  ==>     " + str(automat[key])
