### regex je popis osnovnig skracenica regexa koja se slaze u ostatak automata

#### TODO:
#   [ ]     Povezi ostatak izraza osnovnih regexa u ostatku datoteke
#   [ ]     Stavi svaki izraz u datoteci u dict
#   [ ]     Generiraj automat stanja za svaki regex vezan u kljuc dicta
#   [ ]     Generiraj popis automata prema glavnim stanjima
#   [ ]     Generiraj automat za zadani regex
#   [ ]     Razdovji stanja u zasebne liste
#   [*]     Napravi popis glavnih stanja
#   [*]     Popis lex jedinki za koristenje u lex analizatoru
#
#
#


def ucitajUlaz():
    inputs = []
    regex = {}
    final = ''
    # procitaj ulaznu datoteku definicije jezika, spremi svaki red kao novi clan liste inputs
    while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            final = '\n'.join(inputs)
            break
    print final
    #parsiraj ulaznu datoteku
#    print len(inputs)  ## debug print
    for line in inputs:
        # spremi stanja lex analizatora u listu stanja_lex_analizatora
        if "%X" in line:
            stanja_lex_analizatora = line.split('%X')[1].strip().split(' ')
        # spremi oznake lex jedinki u listu lex_jedinke
        if "%L" in line:
            lex_jedinke = line.split("%L")[1].strip().split(' ')
            break
        # spremi definicije regex izraza u dict regex
        regex[line.split(' ')[0]] = line.split(' ')[1]

    # dopuni regularne izraze (zamjeni skracenice s punim regularnim izrazom)
    for key in regex.keys():
       for reg in regex.keys():
                if key in regex[reg]:
                    regex[reg] = regex[reg].replace(key, "(" + regex[key] + ")")



#    print lex_jedinke  ## debug print
#    print stanja_lex_analizatora   ## debug print

# ako se samostalno ucitava file pokreni ucitajUlaz()
if __name__ == "__main__":
    ucitajUlaz()
