import sys

brRedaka=1
pocetak=0
posljednji=0
zavrsetak=0

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

def fStanja(Qs):
  Fs=[]
  for i in Qs:
    if(i in akcije):
      Fs.append(i)
  Fs.sort()
  return Fs

def akcija(Qs):
  a=akcije[Qs].split(' ')[0]
  if (a!='-'):
    print a+' '+ulaz[pocetak:posljednji]

input = open("tst.in","r")
ulaz = input.read().replace('\n','\\''n')
ulaz = ulaz.replace(' ','\_')

dicPrij={}
akcije={}
automat = open('autom4.txt','r')
dicPrij = prijelazi(automat)
akcije=prijelazi(automat)


while (zavrsetak<len(ulaz)):
#  print len(ulaz)
#  print 'TU SAM'
  Q=['q0']
  Q=eOkruzenje(Q)
  izraz=''
  while(Q):
#    print Q
#    print '*******'
    R=fStanja(Q)
#    print R
#    print '---------'
    if(not R):
      a=ulaz[zavrsetak] #aaa
  #    print zavrsetak
      zavrsetak=zavrsetak+1
      Q=eOkruzenje(prijelaz(Q,a))
    else:
      izraz=R[0]
  #    print izraz
  #    print '////////'
      posljednji=zavrsetak
      if zavrsetak==len(ulaz): break
      a=ulaz[zavrsetak] #bbb
      zavrsetak=zavrsetak+1
      Q=eOkruzenje(prijelaz(Q,a))

  if (not izraz):
    sys.stderr.write(ulaz[pocetak]) #U knjizi red 60 i 61 su:
    pocetak=pocetak+1 #zavrsetak=pocetak
    zavrsetak=pocetak
  else:
    akcija(izraz)
    pocetak=posljednji
    zavrsetak=pocetak
