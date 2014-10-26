### regex je popis osnovnig skracenica regexa koja se slaze u ostatak automata

#[ ] TODO:
#   [*]     Povezi ostatak izraza osnovnih regexa u ostatku datoteke
#   [*]     Stavi svaki izraz u datoteci u dict
#   [ ]     Generiraj automat stanja za svaki regex vezan u kljuc dicta
#   [*]     Generiraj popis automata prema glavnim stanjima
#   [ ]     Generiraj automat za zadani regex
#   [*]     Razdovji stanja u zasebne liste
#   [*]     Napravi popis glavnih stanja
#   [*]     Popis lex jedinki za koristenje u lex analizatoru
automat = {}


def generiraj_lex_automat(lines, current, automat, stanja, regex):
    _state_def = ""
    for line in range (current,len(lines)): # sa svaku liniju u definiciji jezika

        for stanje in stanja:               # provjeri za sva stanja lexanalizatora u popisu stanja lexanalizatora

            if "<"+stanje+">" in lines[line]:       # ako se odnosi na trenutno stanje
                _state_def = lines[line]

                # TODO: treba preraditi spremi definiciju u dict stanja =>> krivo jer ce se prepisati definicija automata
                for key in regex.keys():        #dopuni nazive regexa s punim izrazom
                    if key in _state_def:
                        _state_def =  _state_def.replace(key, "(" + regex[key] + ")") # dopuni ostatak regularnih izraza

                direktive = []
#        line = line + 2
                try:
                    line = line + 2
                    while lines[line].strip() != "}":
                        direktive.append(lines[line])

                        line = line + 1

                    automat[_state_def] = direktive
                except IndexError:
                    break

                print _state_def + ":                       ###<-------------"
                print automat[_state_def]
                # TODO: file regex.py sadrzi generator automata stanja za regularne izraze
                # TODO: povezi automate sa akcijama vezanim uz prihvacene regularne izraze






def ucitajUlaz(automat):
    inputs = []
    regex = {}
    final = ''
    procitao_rex_jedinke = False
    # procitaj ulaznu datoteku definicije jezika, spremi svaki red kao novi clan liste inputs
    while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            final = '\n'.join(inputs)
            break
#    print final ## debug print
    #parsiraj ulaznu datoteku
#    print len(inputs)  ## debug print
    for line in range (len(inputs)):
        if procitao_rex_jedinke:
            # kada procita postavke jezika (lex jedinke, stanja lex automata i definicije reg izraza) napravi DKA glavnih stanja lex analizatora
            generiraj_lex_automat(inputs, line, automat, stanja_lex_analizatora, regex)
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



#    print lex_jedinke  ## debug print
#    print stanja_lex_analizatora   ## debug print

# ako se samostalno ucitava file pokreni ucitajUlaz()
if __name__ == "__main__":
    ucitajUlaz(automat)
