import sys

def prijelaz(Qs,z):
  Rs=[]
  for i in Qs:
    klj=i+'|'+z #stanje|znak   pretpostavio da dict prijelaza je oblika {'q|a':'q1,q2,q3 akcija? akcija?'
    if(klj in dicPrij):
      stanja=dicPrij[klj].split(' ')[0].split(',') #stanja
      for j in stanja:
        Rs.append(j) #dodaj u skup stanja
  return Rs

def eOkruzenje(Qs):
  Rs=[]
  stog=[]
  for i in Qs:
    Rs.append(i)
    stog.append(i)

  while(len(stog)!=0):
    s=stog.pop()  #za svako stanje ustogu e prijelaz
    klj=s+'|'+'$'
    if(klj in dicPrij):
      stanja=dicPrij[klj].split(' ')[0].split(',')
      for g in stanja:
        if (g not in Rs):
          Rs.append(g) #ako nije u skupu dodaj ga
          stog.append(g)
  return Rs

def prijelazi(aut):
  dicPrijelazi={}
  red=aut.readline().rstrip()
  while(red):
    lRed=red.split(' ')
    dicPrijelazi[lRed[0]]=lRed[1]
    red=aut.readline().rstrip() #3 7 15 26 41
  return dicPrijelazi

def akc(aut):
  dicAkcije={}
  red=aut.readline().rstrip()
  while(red):
    lRed=red.split(' ')
    dicAkcije[lRed[0]]=lRed[1:len(lRed)]
    red=aut.readline().rstrip() #3 7 15 26 41
  return dicAkcije

def fStanja(Qs):
  Fs=[]
  for i in Qs:
    if(i in akcije):
      Fs.append(i)
  Fs.sort()
  return Fs

def akcija(Qs):
  global brRedaka
  global pocetak
  global zavrsetak
  global posljednji
  global stanje
  a=akcije[Qs][0]
  if ('VRATI_SE' in akcije[Qs]):
    i=akcije[Qs].index('VRATI_SE')
    pomak=int(akcije[Qs][i+1])
    zavrsetak=pocetak+pomak
    posljednji=zavrsetak
  if (a!='-'):
    print a+' '+str(brRedaka)+' '+ulaz[pocetak:posljednji]
  if ('NOVI_REDAK' in akcije[Qs]):
      brRedaka=brRedaka+1
  if ('UDJI_U_STANJE' in akcije[Qs]):
    i=akcije[Qs].index('UDJI_U_STANJE')
    stanje = akcije[Qs][i+1]

brRedaka=1
pocetak=0
posljednji=0
zavrsetak=0

input = open("tst.in","r")
ulaz = input.read().replace('\n','\\''n')
ulaz = ulaz.replace(' ','\_')

dicPrij={}
akcije={}

automat = open('autom4.txt','r')
pocStanja={}
sta1 = automat.readline().rstrip().split(' ') #stanja automata
pocStanja={}
for i in range(len(sta1)):
  klj = sta1[i].split('|')[0]
  poc =sta1[i].split('|')[1].split(',')
  pocStanja[klj]=poc
  if (1 in poc):
    stanje=klj
print pocStanja



dicPrij = prijelazi(automat)
automat.readline() #ucitavanje prijelaza i pocetnog stanja za jedan e-NKA
akcije=akc(automat) #ucitavanje akcija


while (zavrsetak<len(ulaz)):
  Q=pocStanja[stanje]
  Q=eOkruzenje(Q)
  izraz=''
  while(Q):
    R=fStanja(Q)
    if(not R):
      a=ulaz[zavrsetak]
      zavrsetak=zavrsetak+1
      Q=eOkruzenje(prijelaz(Q,a))
    else:
      izraz=R[0]
      posljednji=zavrsetak
      if zavrsetak==len(ulaz): break
      a=ulaz[zavrsetak]
      zavrsetak=zavrsetak+1
      Q=eOkruzenje(prijelaz(Q,a))

  if (not izraz):
    sys.stderr.write(ulaz[pocetak])
    pocetak=pocetak+1
    zavrsetak=pocetak
  else:
    akcija(izraz)
    pocetak=posljednji
    zavrsetak=pocetak
