### regex je popis osnovnig skracenica regexa koja se slaze u ostatak automata

#[*] TODO:
#   [*]     Povezi ostatak izraza osnovnih regexa u ostatku datoteke
#   [*]     Stavi svaki izraz u datoteci u dict
#   [*]     Generiraj automat stanja za svaki regex vezan u kljuc dicta
#   [*]     Generiraj popis automata prema glavnim stanjima
#   [*]     Generiraj automat za zadani regex
#   [*]     Razdovji stanja u zasebne liste
#   [*]     Napravi popis glavnih stanja
#   [*]     Popis lex jedinki za koristenje u lex analizatoru
#   [*]     Popis prihvatljivih stanja (f stanja)
import regex
from regex import *



automat = {}


def generiraj_lex_automat(lines, current, automat, stanja, regex):
    _state_def = ""
    count_stanja = 0
    line = current
    prioritet = 0
    while line < len(lines):
        for stanje in stanja:               # provjeri za sva stanja lexanalizatora u popisu stanja lexanalizatora

            if "<"+stanje+">" in lines[line]:       # ako se odnosi na trenutno stanje
                _state_def = lines[line]

                # TODO[*]: treba preraditi spremi definiciju u dict stanja =>> krivo jer ce se prepisati definicija automata
                for key in regex.keys():        #dopuni nazive regexa s punim izrazom
                    if key in _state_def:
                        _state_def =  _state_def.replace(key, "(" + regex[key] + ")") # dopuni ostatak regularnih izraza
                direktive = []
                try:
                    line = line + 2
                    direktive.append(prioritet)
                    prioritet += 1
                    while lines[line].strip() != "}":
                        direktive.append(lines[line])

                        line = line + 1

                    automat[_state_def] = direktive
                    count_stanja = count_stanja + 1
                except IndexError:
                    break
                print direktive
        line += 1
    return stanja

                #print"\n" +_state_def
                #printautomat[_state_def]

                # TODO: file regex.py sadrzi generator automata stanja za regularne izraze
                # TODO: povezi automate sa akcijama vezanim uz prihvacene regularne izraze

    #printcount_stanja





def ucitajUlaz(automat):
    inputs = []
    stanja = []
    regex = {}
    procitao_rex_jedinke = False
    # procitaj ulaznu datoteku definicije jezika, spremi svaki red kao novi clan liste inputs
    while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            break


    #parsiraj ulaznu datoteku
#    #printlen(inputs)  ## debug print
    for line in range (len(inputs)):

        if procitao_rex_jedinke:
            # kada procita postavke jezika (lex jedinke, stanja lex automata i definicije reg izraza) napravi DKA glavnih stanja lex analizatora
            stanja = generiraj_lex_automat(inputs, line, automat, stanja_lex_analizatora, regex)
            break
        # spremi stanja lex analizatora u listu stanja_lex_analizatora
        elif "%X" in inputs[line]:
            stanja_lex_analizatora = inputs[line].split('%X')[1].strip().split(' ')
        # spremi oznake lex jedinki u listu lex_jedinke
        elif "%L" in inputs[line]:
            lex_jedinke = inputs[line].split("%L")[1].strip().split(' ')
            procitao_rex_jedinke = True
        # spremi definicije regex izraza u dict regex
        else:

                regex[inputs[line].split(' ')[0]] = inputs[line].split(' ')[1]


    # dopuni regularne izraze (zamjeni skracenice s punim regularnim izrazom)
    for key in regex.keys():
       for reg in regex.keys():
                if key in regex[reg]:
                    regex[reg] = regex[reg].replace(key, "(" + regex[key] + ")")

    return stanja
def dodaj_u_dict(_dict, key, value):
    states = []
    states.append(value)
    if str(key) in _dict.keys():
        states.extend(_dict[key])
    _dict[key] = states

def zapisi_u_file(_dict_main, _dict_stanja):

    outFile = open ("analizator/izlazni.txt", "w")
    for key in _dict_stanja.keys():
        outFile.write(key + "|")
        for stanje in automat_po_stanjima[key]:
            outFile.write(stanje.split(",")[0].split("(")[1].strip() + ",")
        outFile.write(" ")
    outFile.write("\n")


    for key in _dict_main.keys():
        outFile.write(key + ' ' + str(_dict_main[key]).replace("[", "").replace("]", "").replace(" ", "")+ "\n")

    outFile.write("\n###\n")
    for key in _dict_stanja.keys():
        for stanje in _dict_stanja[key]:
            try:
                ##print stanje
                direktiva = stanje.split(")")[1]
                #print direktiva
            except IndexError:
                pass
            outFile.write(stanje.split(",")[1].split(")")[0].strip())

            outFile.write(" ")
            outFile.write(direktiva.replace("[" ,"").replace("]", "").replace("'", "").replace(",",""))
            outFile.write("\n")
                ##print direkt

# ako se samostalno ucitava file pokreni ucitajUlaz()
if __name__ == "__main__":
    regex_automat = {}
    regex_automat[brojac_stanja] = 0
    stanja = []
    stanja = ucitajUlaz(automat)
    automat_po_stanjima= {} ## za svako stanje pise pocetak i kraj automata

    for key in automat.keys():
        #print key
        for stanje in stanja:

            if "<"+ stanje+">" in key:
                regexStanja = key.replace("<"+stanje+">", "")
                dodaj_u_dict(automat_po_stanjima, stanje, str(pretvori(regexStanja, regex_automat)) + str(automat[key]) ) ## pretvori vraca pair prvo i zadnje stanje

    for key in automat_po_stanjima.keys():
        for element in automat_po_stanjima[ key]:
            pass
            #print element
        #print "----------------------------------------"
    zapisi_u_file(regex_automat,automat_po_stanjima)
