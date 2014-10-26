def novo_stanje(brojac):
    brojac += 1
    return brojac
    
    
def je_operator(izraz, pozicija):
    br = 0
    while pozicija-1 >= 0 and izraz[pozicija-1] == '\\':
        br = br + 1
        pozicija -= 1
    return br%2 == 0
    

# napravi prijelaz iz stanja q1 u q2 vezano uz znak znak
def dodaj_prijelaz(automat, q1, q2, znak):
    key = q1 + znak
    automat[key] = q2
    
def nadi_iducu_zagradu(izraz, pozicija):
    br = 1
    for izraz[]