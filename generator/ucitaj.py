### regex je popis osnovnig skracenica regexa koja se slaze u ostatak automata

#### TODO:
#   [ ]     Povezi ostatak izraza osnovnih regexa u ostatku datoteke
#   [ ]     Stavi svaki izraz u datoteci u dict
#   [ ]     Generiraj automat stanja za svaki regex vezan u kljuc dicta
#   [ ]     Generiraj popis automata prema glavnim stanjima
#   [ ]     Generiraj automat za zadani regex
#   [ ]     Razdovji stanja u zasebne liste
#   [*]     Naprapi popis glavnih stanja
#
#
#
#



def ucitajUlaz():
    inputs = []
    popis_mega_stanja = []
    regex = {}
    final = ''
    while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            final = '\n'.join(inputs)
            break
    print final
    
    print len(inputs)
    for line in inputs:
        if "%X" in line:
            break
        regex[line.split(' ')[0]] = line.split(' ')[1]

    for key in regex.keys():  
       for reg in regex.keys():
                if key in regex[reg]:
                    regex[reg] = regex[reg].replace(key, "(" + regex[key] + ")")
                
    for line in inputs:
        if "%X" in line:
            popis_mega_stanja = line.split('%X')[1].strip().split(' ')
            
    print popis_mega_stanja
    
    
    
    
    
    
    
    
    
    
    
    
    
if __name__ == "__main__":
    ucitajUlaz()