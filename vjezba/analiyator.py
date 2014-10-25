import sys

brRedaka=1
pocetak=0; posljednji=0; zavrsetak=0;

def prijelaz(Qs,z):
  Rs=[]
  for i in Qs:
    klj=Qs[i]+'|'+z #stanje|znak   pretpostavio da dict prijelaza je oblika {'q|a':'q1,q2,q3 akcija? akcija?'
    stanja=pri[klj].split(' ')][0].split(',') #stanja
    for j in stanja:
      Rs.append(j) #dodaj u skup stanja
  return Rs

def eOkruzenje(Qs):
  Rs=[]
  stog=[]
  for i in Qs:
    klj=Qs[i]+'|'+'$' #stanje|znak
    stanja=pri[klj].split(' ')][0].split(',') #stanja prvog e prijelaza
    for j in stanja:
      Rs.append(j) #dodaj u listu stanja
      stog.append(j) #dodaj u stog
  while(len(stog)!=0):
    s=stog.pop()  #za svako stanje ustogu e prijelaz
    klj=s+'|'+'$'
    stanja=pri[klj].split(' ')][0].split(',')
    for g in stanja:
      jePris=0
      for h in range(len(Rs)):
        if (g==Rs[h]):  #ako je novo stanje vec u skupu netreba ga dodavat
          jePris=1
          break
    if (jePris==0):
      Rs.append(g) #ako nije u skupu dodaj ga
      stog.append(g) #dodaj u stog za daljnje e prijelaze

def fStanja(Qs):
    pass
def minStanje(Qs):
    pass
    
def main():
  input = open("test.lan","r")
  ulaz = input.read().replace('\n','\\''n')

  #Tu bi trebalo doc poziv funkcije za izgranju dic automata


  while (zavrsetak<len(ulaz)):
    Q=[q0]
    Q=eOkruzenje(Q)
    izraz=''
    while(len(Q)!=0):
      R=fStanja(Q)
      if(len(R)==0):
        a=ulaz[zavrsetak]
        zavrsetak++
        Q=eOkruzenje(prijelaz(Q,a))
      else:
        izraz=minStanje(R)
        posljednji=zavrsetak
        zavrsetak++
        a=ulaz[zavrsetak]
        Q=eOkruzenje(prijelaz(Q,a))

    if izraz:
      sys.stderr.write(ulaz[pocetak]'\n') #U knjizi red 60 i 61 su:
      pocetak++ #zavrsetak=pocetak
      zavrsetak=pocetak #pocetak++  al meni to nema smisla
    else:
      Akcija(izraz)
      pocetak=posljednji+1 #i ovdje
      zavrsetak=pocetak #zavrsetak=posljednji
