# kao neki brojac stanja u automatu
def novo_stanje(automat):
    automat["brojac_stanja"] = automat["brojac_stanja"] + 1
    return automat[brojac_stanja]



# prebroji koliko ima \ u nizu prije znaka, ukoliko je broj paran (\\) onda je operator
# ukoliko je broj \ neparan (\) ona je znak, npr. \( -> je oznaka za zagradu dok je ( operator selekcije u izrazu ()
# \ se koristi kao escape oznaka, npr u C-u \\ -> znaci \, \n -> novi red \t -> tab \" navodnik unutar stringa print ("\"") -> "
def je_operator(izraz, i):
    br = 0
    while i-1 >= 0 and izraz[i-1]=='\\': # broji escape oznake, ukoliko se pojavi nesto sto nije \ onda prekini provjeru
        br = br + 1
        i = i - 1       # gledamo unazad od znaka koji provjeravam
    return br%2 == 0    # ukoliko je broj znakova \ paran onda je znak operator, inace je znak


def dodaj_prijelaz(automat ,stanje1, stanje2, znak):
    states = []
    states.append(stanje2)
    if str(stanje1)+"|"+znak in automat.keys():
        states.extend(automat[str(stanje1) + "|" + znak])
        print "here "
    automat[str(stanje1)+"|"+znak] = states


def nadi_iducu_zagradu(izraz, i):
   # print izraz
    br_zagrada = 1
    for j in range( len (izraz[i+1:])):
        if izraz[j] == ")" and je_operator (izraz, j):
            br_zagrada -= 1
            if br_zagrada == 0:
                return j
        elif izraz[j] == "(" and je_operator(izraz, j):
            br_zagrada += 1

    return i





    # automat ce biti dict automat, ime dicta ce biti genericko i vezano uz stanje -> dict(stanje lex analizatora, dict automata)


def pretvori(izraz, automat):

    print str(izraz) + "  <=================   pretvori"
    e = "$"
    izbori = []
    elementi = []
    br_zagrada = 0 # pobroji kolicinu zagrada zasto se broje zagrade i kako se pretvaraju
    _a = 0
    fin = 0
    pronadjen_barem_jedan_operator = False
# ===============v==========v=============v==========radi=========v======v======v========
    for i in range(len(izraz)):

        if izraz[i] == '(' and je_operator(izraz, i): # provjeri je li trenutni znak operator otvorena zagrada (
            br_zagrada += 1

        elif izraz[i] == ')' and je_operator(izraz, i):  # provjeri je li trenutni znak operator zatvorena zagrada )
            br_zagrada -= 1
            # ako naidjes na izraz oblika (ab)|c razdvoji izraz na ['(ab)', 'c']
        elif br_zagrada == 0 and izraz[i] == '|' and je_operator(izraz, i):
            izbori.append(izraz[_a:i])

            pronadjen_barem_jedan_operator = True
            _a=i+1
        fin = i+1
    izbori.append(izraz[_a:fin])
    lijevo_stanje = novo_stanje(automat)
    desno_stanje = novo_stanje(automat)
    if pronadjen_barem_jedan_operator:
        #==================^=======^===============^=========^==========^=====================


        for element in izbori:
           # print element + "<-----------------    element"
            print str(izbori) + "<////////////////////////////////// izbori i fali zadnji clan izraza"
            print element
            _temp = pretvori(element ,automat)
            # povezi nove automate s starim automatima
            dodaj_prijelaz(automat, lijevo_stanje, _temp[0], e)
            dodaj_prijelaz(automat, _temp[1], desno_stanje, e)
    else:
        prefiksirano = False
        zadnje_stanje = lijevo_stanje
        i=0
        while i < (len(izraz)):


            if prefiksirano:
                # slucaj 1
                prefiksirano = False
                if izraz[i] == 't':
                    prijelazni_znak = '\t' # oznaka za tabu u C-u
                elif izraz[i] == 'n':
                    prijelazni_znak = '\n'
                elif izraz[i] == '_':
                    prijelazni_znak = ' '
                else:
                    prijelazni_znak = izraz[i]
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_prijelaz(automat, a, b, prijelazni_znak)#, prijelazn_znak)


            else:
                if izraz[i] == "\\":
                    prefiksirano = True
                    continue

                if izraz[i] != "(":
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    if izraz[i] == "$":
                        dodaj_prijelaz(automat, a, b, e)
                    else:
                        dodaj_prijelaz(automat, a, b, izraz[i])
                else:
                    j = nadi_iducu_zagradu(izraz, i)
                    _temp = pretvori( izraz[i+1:j-1], automat)
                    a = _temp[0]
                    b = _temp[1]
                    i = j


            if i+1 < (len(izraz)) and izraz[i+1] == '*':
                print "i have it"
                x=a
            
                y=b
                a = novo_stanje(automat)
                b = novo_stanje(automat)
                print str(a) + ' ' + str(b) + " " + str(x) + " " + str(y)
                dodaj_prijelaz(automat, a, x, e)
                dodaj_prijelaz(automat, y, b, e)
                dodaj_prijelaz(automat, a, b, e)
                dodaj_prijelaz(automat, y, x, e)
                i = i+1
                print automat

            dodaj_prijelaz(automat, zadnje_stanje, a, e)
            zadnje_stanje = b
            i += 1
        # end of while

        dodaj_prijelaz(automat, zadnje_stanje, desno_stanje, e)
    print str(( lijevo_stanje, desno_stanje)) + "<|||| tu smo"
    return (lijevo_stanje, desno_stanje)

brojac_stanja = "brojac_stanja"

automat = {}
automat[brojac_stanja] = 0
if __name__ == "__main__":
    print pretvori("a|b*", automat)
    for key in automat.keys():
        print str(key) + ":  ==>     " + str(automat[key])
