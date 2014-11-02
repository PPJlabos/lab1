# kao neki brojac stanja u automatu
def novo_stanje(automat):
    automat["brojac_stanja"] = automat["brojac_stanja"] + 1
    return automat[brojac_stanja]



# prebroji koliko ima \ u nizu prije znaka, ukoliko je broj paran (\\) onda je operator
# ukoliko je broj \ neparan (\) ona je znak, npr. \( -> je oznaka za zagradu dok je ( operator selekcije u izrazu ()
# \ se koristi kao escape oznaka, npr u C-u \\ -> znaci \, \n -> novi red \t -> tab \" navodnik unutar stringa ###print("\"") -> "
def je_operator(izraz, i):
    brojac = 0
    # count backwards the '\' sign until something else comes up
    while i-1 >= 0 and izraz[i-1]=='\\':
        brojac = brojac + 1
        i = i - 1
        # if number of "\" characters is pair the the sign is not escaped
    return brojac%2 == 0


def dodaj_prijelaz(automat ,stanje1, stanje2, znak):
    #add new state to transition list of FMS
    states = []

    # add new state to the list
    states.append(stanje2)

    # if transition already exists then save all old states and add new one
    if str(stanje1)+"|"+znak in automat.keys():
        states.extend(automat[str(stanje1) + "|" + znak])
    # save new transition definition to states table
    automat[str(stanje1)+"|"+znak] = states


def nadi_iducu_zagradu(izraz, i):

    # count brackets until you find new matching one
    #print__name__
    #printi
    #printizraz + "         << ajmo nac neku zagradu"
    br_zagrada = 0

    #for j in range( len (izraz(i:))):
    while i < len(izraz):
        #printi
        if izraz[i] in ")" and je_operator (izraz, i):
            br_zagrada = br_zagrada - 1
            if br_zagrada == 0:
                return i
        elif izraz[i] in "(" and je_operator(izraz, i):
            br_zagrada += 1
        i = i +1
    # if all else fails return original character
    #print" oops i found nothing <<<<<<<<<"
    return i

def pretvori(izraz, automat):
    ##printizraz + "         << pretvori(izraz, automat) -> izraz   line: 52"
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
            ##printizbori
            pronadjen_barem_jedan_operator = True
            _a=i+1
        fin = i+1

    izbori.append(izraz[_a:fin])
    lijevo_stanje = novo_stanje(automat)
    desno_stanje = novo_stanje(automat)

    if pronadjen_barem_jedan_operator:
        for element in izbori:
            ##printelement + "           _temp = pretvori(element, automat) -> element    line: 82"
            _temp = pretvori(element ,automat)
            # povezi automate
            dodaj_prijelaz(automat, lijevo_stanje, _temp[0], e)
            dodaj_prijelaz(automat, _temp[1], desno_stanje, e)
    else:
        prefiksirano = False
        zadnje_stanje = lijevo_stanje
        i=0
        while i < (len(izraz)):
            #printizraz[i] + "           za i=     " + str(i)

            if prefiksirano:
                # slucaj 1
                prefiksirano = False
                if izraz[i] == 't':
                    prijelazni_znak = '\\' # oznaka za tabu u C-u
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_prijelaz(automat, a, b, prijelazni_znak)
                    dodaj_prijelaz(automat, zadnje_stanje, a, e)    # TODO: provjeri funkcionalnost ove linije
                    zadnje_stanje = b
                    prijelazni_znak = "t"

                elif izraz[i] == 'n':
                    prijelazni_znak = '\\'
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_prijelaz(automat, a, b, prijelazni_znak)
                    dodaj_prijelaz(automat, zadnje_stanje, a, e)    # TODO: provjeri funkcionalnost ove linije
                    zadnje_stanje = b
                    prijelazni_znak = "n"

                elif izraz[i] == '_':
                    prijelazni_znak = '\\'
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    dodaj_prijelaz(automat, a, b, prijelazni_znak)
                    dodaj_prijelaz(automat, zadnje_stanje, a, e)    # TODO: provjeri funkcionalnost ove linije
                    zadnje_stanje = b
                    prijelazni_znak = "_"

                else:
                    prijelazni_znak = izraz[i]
                a = novo_stanje(automat)
                b = novo_stanje(automat)
                dodaj_prijelaz(automat, a, b, prijelazni_znak)#, prijelazn_znak)


            else:
                if izraz[i] == "\\":
                    prefiksirano = True
                    i = i+1
                    continue

                if izraz[i] not in  "(":
                    a = novo_stanje(automat)
                    b = novo_stanje(automat)
                    if izraz[i] == "$":
                        dodaj_prijelaz(automat, a, b, e)
                    else:
                        dodaj_prijelaz(automat, a, b, izraz[i])
                elif izraz[i] in "(":
                    j = nadi_iducu_zagradu(izraz, i)
                    ##printizraz[i+1:j] + "                <<< _temp = pretvori(izraz[i+1:j], automat)   -> izraz[i+1:j-1]   linija: 124"
                    _temp = pretvori( izraz[i+1:j], automat)
                    a = _temp[0]
                    b = _temp[1]
                    ##print"            >>>>>" + str(j) + "<<<<< string "
                    i = j



            if i+1 < (len(izraz)) and izraz[i+1] == '*':
                ###print"i have it"
                x=a

                y=b
                a = novo_stanje(automat)
                b = novo_stanje(automat)
                ###printstr(a) + ' ' + str(b) + " " + str(x) + " " + str(y)
                dodaj_prijelaz(automat, a, x, e)
                dodaj_prijelaz(automat, y, b, e)
                dodaj_prijelaz(automat, a, b, e)
                dodaj_prijelaz(automat, y, x, e)
                i = i+1
                ###printautomat

            dodaj_prijelaz(automat, zadnje_stanje, a, e)    # TODO: provjeri funkcionalnost ove linije
            zadnje_stanje = b
            i += 1
        # end of while

        dodaj_prijelaz(automat, zadnje_stanje, desno_stanje, e)
    ###printstr(( lijevo_stanje, desno_stanje)) + "<|||| tu smo"
    return (lijevo_stanje, desno_stanje)

brojac_stanja = "brojac_stanja"

automat = {}
automat[brojac_stanja] = 0
if __name__ == "__main__":
    pass
    #printpretvori(raw_input("enter regex here >"), automat)
    #for key in automat.keys():
        #printstr(key) + ":  ==>     " + str(automat[key])
