import sys

def prijelaz(Qs,z):
  Rs=[]
  if(z=='$'):
    z='$$'

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
 #print dicAkcije
  return dicAkcije

def fStanja(Qs):
  Fs=[]
  Rs=[]
  for i in Qs:
    if(i in akcije):
      Fs.append(akcije[i][0]+'|'+i)
  Fs.sort()
  for j in Fs:
    temp=j.split('|')[1]
    Rs.append(temp)

  return Rs

def akcija(Qs):
  global brRedaka
  global pocetak
  global zavrsetak
  global posljednji
  global stanje
  a=akcije[Qs][1]
  if ('VRATI_SE' in akcije[Qs]):
    i=akcije[Qs].index('VRATI_SE')
    pomak=int(akcije[Qs][i+1])
    zavrsetak=pocetak+pomak
    posljednji=zavrsetak
  if (a!='-'):
    # print "hello"     neki debug print
    print a+' '+str(brRedaka)+' '+ulaz[pocetak:posljednji].replace('\_',' ')
  if ('NOVI_REDAK' in akcije[Qs]):
      #print akcije[Qs]
      brRedaka=brRedaka+1
  if ('UDJI_U_STANJE' in akcije[Qs]):
    i=akcije[Qs].index('UDJI_U_STANJE')
    stanje = akcije[Qs][i+1]

brRedaka=1
pocetak=0
posljednji=0
zavrsetak=0
inputs=[]
def ucitaj_stdin():

     while True:
        try:
            inputs.append(raw_input())
        except EOFError:
            break
     final = '\n'.join(inputs)
     return final

#input = open("tst.in","r")

ulaz = ucitaj_stdin().replace('\n','\\''n')
ulaz = ulaz.replace('\t','\\''t')
ulaz = ulaz.replace(' ','\_')

#print ulaz

dicPrij={}
akcije={}

automat = open('izlazni.txt','r')
pocStanja={}
states = automat.readline().rstrip().split(' ') #stanja automata #sto se ucitava?? #Kako izgleda original?

pocStanja={}
stanje=''
for state in states:
  klj = state.split('|')[0]
  poc = state.split('|')[1].split(',')
  pocStanja[klj]=poc
  #print poc
  #print ('1' in poc)
  #print "\n\n\n"

  if ('1' in poc):
    stanje=klj

dicPrij = prijelazi(automat)
automat.readline() #ucitavanje prijelaza i pocetnog stanja za jedan e-NKA
akcije=akc(automat) #ucitavanje akcija

while (zavrsetak<len(ulaz)):
  #print stanje
  Q=pocStanja[stanje]
  Q=eOkruzenje(Q)
  izraz=''
  while(Q):
    R=fStanja(Q)
    #print str(R) + "                      << this is sparta"
    if(not R):
      if zavrsetak==len(ulaz): break
      a=ulaz[zavrsetak] #aaa
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
    #sys.stderr.write(ulaz[pocetak])
    #print str(pocetak) + "   <--------------------------------------------------- pocetak" #debug print
    pocetak=pocetak+1
    zavrsetak=pocetak
  else:
    #print "<<<<<<<<<<<<<<<<<<<<          " + str(izraz)
    akcija(izraz)
    pocetak=posljednji
    zavrsetak=pocetak
